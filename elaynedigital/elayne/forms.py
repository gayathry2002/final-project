from django import forms
from. models import *

class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact_us
        fields='__all__'