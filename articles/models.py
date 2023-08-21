from django.db import models


class Article(models.Model):
    # https://docs.djangoproject.com/fr/3.1/ref/models/fields/#field-types
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    slug = models.SlugField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(default='default.jpg')#Au cas où on n'a pas d'image il nous renvoie l'image par défaut

    def __str__(self):
        return self.titre