from django.forms import ModelForm, SelectDateWidget
from appvac.models import Client


class CreateNewClient(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'birth_date', 'gender', 'mother_name', 'phone', 'town', 'compound']
        widgets = {
            'birth_date': SelectDateWidget(years=range(2004, 2022))
        }
