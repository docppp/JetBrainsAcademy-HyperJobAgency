"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from menu.views import homepage_view
from menu.views import home_view
from menu.models import SignupView
from menu.models import LoginView
from vacancy.views import vacancy_view, vacancy_new_view
from resume.views import resume_view, resume_new_view

urlpatterns = [
    path('', homepage_view, name='home'),
    path('home/', home_view),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('vacancies/', vacancy_view),
    path('vacancy/new', vacancy_new_view),
    path('resumes/', resume_view),
    path('resume/new', resume_new_view),
    path('admin/', admin.site.urls),
]
