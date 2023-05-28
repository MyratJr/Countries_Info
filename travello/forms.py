from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class RegistrationForm(forms.Form):

    Username=forms.CharField(max_length=100,
                        widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':"Username"
                            }))
    Phone=forms.CharField(max_length=17,
                        widget=forms.NumberInput(attrs={
                                'class':'form-control',
                                'placeholder':"Phone"
                            }))
    Email=forms.EmailField(
                        widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':"Email"
                            }))


class SearchPlace(forms.Form):
    Name=forms.CharField(max_length=40,
                        widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Search place'
                        }))