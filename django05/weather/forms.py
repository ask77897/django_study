from django.forms import ModelForm, TextInput
from .models import City

class Cityform(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widget = {
            'name' : TextInput(attrs={'class' : 'input', 'placeholder' : '도시를 입력하세요.'}),
        }
        
    def clean_name(self):
        name =self.cleaned_data['name']
        if City.objects.filter(name=name).exists():
            raise forms.ValidationError("이미 입력한 도시입니다.")
        return name