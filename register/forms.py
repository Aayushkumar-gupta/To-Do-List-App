from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      # This adds an email field to the registration form.

    class Meta:
        model = User    # This tells Django that the form is associated with the User model.
        fields = ['username', 'email', 'password1', 'password2']    # This defines which fields will appear in the form