from django import forms
from .models import Cow
from .models import MilkRecord

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['name', 'breed', 'milk_production', 'weight', 'health']

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['date', 'quantity']