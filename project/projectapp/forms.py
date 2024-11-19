from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'is_published',
                  'create_date', 'like_count',]
