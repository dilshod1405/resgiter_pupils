from django.shortcuts import render, redirect

from .forms import PupilForm
from .models import Pupil


def pupils(request):
    a = Pupil.objects.all()
    return render(request, 'registration/pupils.html', {
        'a': a,
    })


def registration(request):
    if request.method == 'GET':
        form = PupilForm()
    else:
        form = PupilForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save(data)
    return render(request, 'registration/index.html', {
        'form': form,
    })
