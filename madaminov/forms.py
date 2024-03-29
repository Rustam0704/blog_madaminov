from django import forms
from django.core.exceptions import ValidationError

from madaminov.models import Post, Author, About


class PostCreateForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ["title", "content"]

class AboutCreateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ["title", "description"]


class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1==password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            return ValidationError("Password must be match")

    class Meta:
        model = Author
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)