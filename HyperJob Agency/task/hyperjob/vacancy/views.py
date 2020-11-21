from django.http import HttpResponse
from django.shortcuts import render
from .models import Vacancy, VacancyForm
from django.http import HttpResponseRedirect

vacancyManager = Vacancy.objects

var = {'vacancies': vacancyManager.all()}


def vacancy_view(request, *args, **kwargs):
    return render(request, "vacancy.html", var)


def vacancy_new_view(request, *args, **kwargs):
    if request.method == 'POST':

        if not request.user.is_staff:
            return HttpResponse(status=403)

        if not request.user.is_authenticated:
            return HttpResponse(status=403)

        desc = request.POST.get('description')
        Vacancy.objects.create(author=request.user, description=desc)
        return HttpResponseRedirect('/home')

    vacancy_form = VacancyForm()
    context = {'vacancy_form': vacancy_form}
    return render(request, "vacancy_new.html", context)

