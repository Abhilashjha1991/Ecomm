from django import forms
# from .models import Cart




PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]
class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                        required=False,
                                      coerce=int)#coerce will conver choice input into integer
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
'''
class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields="__all__"
'''