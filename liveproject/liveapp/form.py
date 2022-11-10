from dataclasses import fields
from django import forms
from django import forms
from liveapp.models import student


class studentRegister(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"