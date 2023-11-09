from django import forms
from .models import PriceBid

class NewPriceBidForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     initial_company = kwargs.pop('initial_company', None)  # Get the initial value for 'company'
    #     super(NewPriceBidForm, self).__init__(*args, **kwargs)
    #     if initial_company is not None:
    #         self.fields['company'].initial = initial_company
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Text k řádkům nabídky'}))
    class Meta:
        model = PriceBid
        fields = ('number', 'parts', 'text', 'customer_type', 'company')