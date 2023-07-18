from .models import Comment 
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'cantact'}),
            'body':forms.Textarea(attrs={'class':'style-body'}),
            
        }

       