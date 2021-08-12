from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'email', 'name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"