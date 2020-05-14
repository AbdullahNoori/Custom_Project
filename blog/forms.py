from django import forms
from blog.models import Blog


class BlogForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ["author"]