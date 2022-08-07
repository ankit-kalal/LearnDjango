from dataclasses import fields
import email
from django import forms
from django.core.validators import RegexValidator
from .models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=5,required=True)
    # phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    # phone = forms.CharField(max_length=255, required=True, validators=[phone_regex])
    # query = forms.CharField(widget = forms.Textarea)