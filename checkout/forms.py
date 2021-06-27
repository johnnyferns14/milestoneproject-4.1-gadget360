from django import forms
from .models import OrderDetail


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ('cust_name', 'email_id', 'contact_number', 'address1',
                  'address2', 'town_or_city', 'postcode', 'country',
                  'county')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'cust_name': 'Name',
            'email_id': 'Email Id',
            'contact_number': 'Phone Number',
            'address1': 'Address',
            'address2': 'Adress2(Optional)',
            'town_or_city': 'Town/City',
            'postcode': 'Postcode',
            'country': 'Country',
            'county': 'County'
        }

        self.fields['çust_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
