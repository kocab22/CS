from django import forms
from .models import PriceBid
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineRadios #todo try to format inlne / how ?



class NewPriceBidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Uložit'))
       
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Text k řádkům nabídky'}))
    customer_type = forms.ChoiceField(choices=PriceBid.CustomerChoices.choices, widget=forms.RadioSelect, initial='RG')
    class Meta:
        model = PriceBid
        fields = ('number', 'parts', 'text', 'customer_type', 'company')