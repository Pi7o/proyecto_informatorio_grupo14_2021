from typing_extensions import Required
from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        exclude = ['hidden', 'author', 'slug']
        labels = {
            'title': _('Titulo'),
            'content': _('Contenido'),
            'thumbnail': _('Imagen'),
            'post_tag': _('Tag')

        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))

    class Meta:
        model = Comment
        fields = ('content', )
        labels = {
            'content': _('Comentario')
        }
