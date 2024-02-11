from django import forms
from django.forms import ModelForm

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields= ('category','title','content','img')

        widgets ={
            #'category':forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-select shadow rounded-0','placeholder': 'Select a Category'}), 
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'rows':'8','cols':'10','class':'form-control'}),

        }
