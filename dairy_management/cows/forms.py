from django import forms
from .models import Cow
from .models import MilkRecord

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['name', 'breed', 'date_of_birth', 'weight', 'health']

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['date', 'quantity']