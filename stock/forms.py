from django import forms
from .models import ItemCode

class ItemCodeForm(forms.ModelForm):
    class Meta:
        model = ItemCode
        fields = [
            'number',
            # 'barcode',
        ]