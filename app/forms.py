"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import Food,Customer

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class Itemform(forms.ModelForm):
    food_name = forms.CharField()
    food_description = forms.CharField()
    food_price = forms.DecimalField(min_value=0, max_value=1000)
    food_available = forms.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = Food
        fields = ['food_name', 'food_description', 'food_price', 'food_available']


class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField()
    customer_address = forms.CharField()
    customer_phone = forms.CharField()

    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_address', 'customer_phone']

