

from django import forms 
from myapp.models import Imgsave1

class ImgsaveForm(forms.ModelForm):
    class Meta:
        model=Imgsave1
        fields=('id','name','file1','value')

