# coding=utf-8
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=128, label='Temat')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Treść')