from django.forms import ModelForm, TextInput, NumberInput, DateField, SelectDateWidget
from front.models import period


class periodForm(ModelForm):
    
    class Meta():
        model = period
        fields = ('start_date','end_date','is_active')
         