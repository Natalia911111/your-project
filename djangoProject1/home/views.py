from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms


# Create your views here.


def home(request):
    # return HttpResponse("Hello")
    return render(request, 'home/index.html')


def contact(request):
    form = forms.ContactMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    return render(request, 'home/contact.html', {
        "form": form
    })
