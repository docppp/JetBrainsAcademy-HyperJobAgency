from django.http import HttpResponse
from django.shortcuts import render
from .models import Resume, ResumeForm
from django.http import HttpResponseRedirect


def resume_view(request, *args, **kwargs):
    resumeManager = Resume.objects
    var = {'resumes': resumeManager.all()}
    return render(request, "resume.html", var)


def resume_new_view(request, *args, **kwargs):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            return HttpResponse(status=403)

        desc = request.POST.get('description')
        r = Resume(author=request.user, description=desc)
        r.save()
        return HttpResponseRedirect('/home')

    resume_form = ResumeForm()
    context = {'resume_form': resume_form}
    return render(request, "resume_new.html", context)
