from django import forms
from django.contrib.auth.models import User


class BookLendForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects, label='')
