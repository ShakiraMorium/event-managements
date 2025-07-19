from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')  

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Username',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Email',
                'required': True,
            }),
            'role': forms.Select(attrs={
                'class': 'select select-bordered w-full',
                'required': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply styles to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Password',
            'required': True,
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Confirm Password',
            'required': True,
        })

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input input-bordered w-full',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input input-bordered w-full',
        'placeholder': 'Password'
    }))