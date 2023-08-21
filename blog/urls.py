from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static #On doit importer static pour créer une url static à partir des variables dans settings

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('remerciements/', views.remerciements_view, name='remerciements'),
    path('articles/', include('articles.urls'), name='articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Pour avoir accès aux images sur le navigateur
