from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *

from accounts.models import CustomUser,Seller,SellerAdditional

class ContactUsForm(forms.ModelForm):
# class ContactUsForm(forms.Form):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=5, required=True)
    
    # phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    # phone = forms.CharField(max_length=255, required=True, validators=[phone_regex])
    # query = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Contact
        fields = '__all__'




class RegistrationFormSeller(forms.ModelForm):
    class Meta:
        model = SellerAdditional
        fields = [
            'gst',
            'warehouse_location'
        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
        ]

# class RegistrationForm(UserCreationForm):
#     gst = forms.CharField(max_length=10)
#     warehouse_location = forms.CharField(max_length=1000)
#     class Meta:
#         model = Seller
#         # model = User
#         fields = [
#             'email',
#             'name',
#             'gst',
#             'warehouse_location',
#             'password1',
#             'password2',
#         ]