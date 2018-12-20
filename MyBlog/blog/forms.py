from django import forms
from blog.models import Post,Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('title','text')

        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent','id':'bord'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('text',)

        widgets={
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
