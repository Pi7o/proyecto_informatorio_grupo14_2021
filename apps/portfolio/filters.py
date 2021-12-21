from django.db.models import fields
import django_filters
from django_filters.filters import DateFilter, CharFilter
from django.utils.translation import gettext_lazy as _

from .models import *


class PostFilter(django_filters.FilterSet):

    title = CharFilter(field_name='title',
                       lookup_expr='icontains', label='Titulo')
    posttag = CharFilter(field_name='post_tag',
                         lookup_expr='icontains', label='Tag')
    start_date = DateFilter(label='Desde', field_name="timestamp",
                            lookup_expr='gte')
    end_date = DateFilter(label='Hasta', field_name="timestamp",
                          lookup_expr='lte')

    class Meta:

        model = Post

        fields = ('author',)
        labels = {
            'author': _('Autor'),
        }

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['author'].extra.update(
            {'empty_label': 'Todos'})


class CommentFilter(django_filters.FilterSet):
    comentario = CharFilter(field_name='content',
                            lookup_expr='icontains', label='Comentario')

    class Meta:
        model = Comment

        fields = ('user',)
        labels = {
            'user': _('Usuario'),
        }
