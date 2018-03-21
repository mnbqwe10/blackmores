from django import forms

class SKUForm(forms.Form):
    input_sku = forms.CharField(label='Add SKU', max_length=100)
