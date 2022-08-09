from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Members

class MembersForm(UserCreationForm):
    class Meta:
        model = Members
        fields = ['username', 'password1', 'password2', 'member_name', 'sex', 'phone_number', 'introduce']


class MembersModifyForm(UserCreationForm):
    class Meta:
        model = Members
        fields = ['password1', 'password2', 'member_name', 'sex', 'phone_number', 'introduce']

# class SignInForm(UserCreationForm):
#     class Meta:
#         model = Members
#         fields = ['username', 'password']


