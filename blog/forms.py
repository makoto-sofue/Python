from django import forms 
from .models import Commment


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):   #全ての属性にform-controlを入れる
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



    class Meta:
        model = Commment
        fields = ('name', 'text')
