"""overide form for sign-in, sign-up pages"""
from django import forms
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


# class SignInForm(forms.Form):
#     """overide sign in form"""
#     def __init__(self, *args, **kwargs):
#         super()


class CustomSignupForm(SignupForm):
    """custom signup without new field"""

    def save(self, request):
        """add user to editor group by default"""
        user = super(CustomSignupForm, self).save(request)
        group, created = Group.objects.get_or_create(name="Editor")
        if created:
            user.groups.add(group)
        return user