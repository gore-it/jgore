# coding=utf-8
from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['admin@jgore.pl'],
            )
            return HttpResponseRedirect('/kontakt')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})