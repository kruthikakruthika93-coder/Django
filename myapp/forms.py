from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item       # <-- Notice 'model' is lowercase now
        fields = ['name']