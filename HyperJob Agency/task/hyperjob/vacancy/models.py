from django.db import models
from django.contrib.auth.models import User
from django import forms


class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class VacancyForm(forms.Form):
    author = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1024)
