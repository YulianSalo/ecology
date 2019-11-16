from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import *
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

#class SignUpForm(UserCreationForm):
class SignUpForm(forms.ModelForm):

    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    userPassword= forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    def clean_password2(self):
        userPassword = self.cleaned_data.get("userPassword")
        password2 = self.cleaned_data.get("password2")
        if userPassword and password2 and userPassword != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    class Meta:
    	model = userProfile
    	fields = ('userClass', 'userLogin', 'userEmail', 'userPassword', 'password2')	