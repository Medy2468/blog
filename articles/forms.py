from django.forms import ModelForm
#Pour avoir accès à tous nos types de formulaires déclarés dans le model
from .models import Article


class ArticleForm(ModelForm):
    class Meta: #Cette class nous permet de modifier un certain nombres de variables de classe
        model = Article
        fields = ['titre', 'contenu', 'slug', 'image']