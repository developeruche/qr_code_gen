from django import forms
from . import models

class CreateQrCode(forms.ModelForm):
    class Meta:
        model = models.QrDetails
        fields = ['text']
