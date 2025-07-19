
from django.contrib.auth.decorators import user_passes_test

def organizer_required(view_func):
    decorator = user_passes_test(lambda u: u.is_authenticated and u.role == 'organizer')
    return decorator(view_func)
