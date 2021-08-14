from django import forms
from .models import Comment, Post, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']

        widgets = {
			"name": forms.TextInput(attrs= { 
				'name' : 'name',
				'class': 'form-control',
				'id': 'firstName',
				'required' : True
			}),
			"email": forms.EmailInput(attrs= { 
				'name' : 'email',
				'class': 'form-control',
				'id': 'email',
				'required' : True
			}),
			"content": forms.Textarea(attrs= { 
				'name' : 'content',
				'class': 'form-control',
				'id': 'content',
				'rows' : 5,
				'columns': 5,
				'required' : True
			}),

		}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class AdminLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"

		widgets = {
			"first_name": forms.TextInput(attrs= { 
				'name' : 'firstName',
				'class': 'form-control',
				'id': 'firstName',
				'required' : True
			}),
			"email": forms.EmailInput(attrs= { 
				'name' : 'email',
				'class': 'form-control',
				'id': 'email',
				'required' : True
			}),
			"message": forms.Textarea(attrs= { 
				'name' : 'message',
				'class': 'form-control',
				'id': 'message',
				'rows' : 5,
				'columns': 5,
				'required' : True
			}),

		}