from django import forms

from blog.models import BlogComment


class BlogCommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'comment_hidden'}), required=False)

    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'comment']
