from django import forms
from django.forms import Textarea
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ('nome', 'descricao', 'foto')
        widgets = {
            'descricao': Textarea(attrs={'cols': 50, 'rows': 8}),
        }