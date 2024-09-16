from django import forms

class CurrencyConversionForm(forms.forms):
    amount = forms.DecimalField(label='Amount', decimal_places=2, max_digits=10)
    from_currency = forms.CharField(label='From Currency', max_length=3)
    to_currency = forms.CharField(label='To Currency', max_length=3)