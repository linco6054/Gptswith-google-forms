from django.forms import ModelForm, TextInput, NumberInput, DateField, SelectDateWidget
from front.models import period , category


class periodForm(ModelForm):
    
    class Meta():
        model = period
        fields = '__all__'
         
         

class categoryForm(ModelForm):
    
    class Meta():
        model = category
        fields = '__all__'
        exclude = ['created_by']   