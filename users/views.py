from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()  

# Activation View
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated. Please log in.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid or has expired.")
        return render(request, 'users/activation_failed.html')

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('users/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'admin@ems.com', [user.email])
            return redirect('email-sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/sign_up.html', {'form': form})

# Sign In View (with email login)
def login_view(request):
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    error_message = 'Invalid credentials.'
            except User.DoesNotExist:
                error_message = 'User does not exist.'
    else:
        form = LoginForm()
    return render(request, 'users/sign_in.html', {'form': form, 'error_message': error_message})

#Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
