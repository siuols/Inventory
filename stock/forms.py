from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
	        'brand',
			'category',
			'number',                 
			'name',                   
			'description',             
			'quantity',               
			'unit_cost',   
        ]