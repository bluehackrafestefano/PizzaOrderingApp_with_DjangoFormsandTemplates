from django import forms
from .models import Pizza, Size, Topping


class PizzaForm(forms.ModelForm): 
    size = forms.ModelChoiceField(queryset=Size.objects, widget=forms.RadioSelect)
    topping = forms.ModelMultipleChoiceField(queryset=Topping.objects, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Pizza
        fields = ('size', 'topping')
