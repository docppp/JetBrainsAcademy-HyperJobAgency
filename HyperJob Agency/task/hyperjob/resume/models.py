from django.db import models
from django.contrib.auth.models import User
from django import forms


class Resume(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.TextField(max_length=1024)


class ResumeForm(forms.Form):
    description = forms.CharField(max_length=1024)
