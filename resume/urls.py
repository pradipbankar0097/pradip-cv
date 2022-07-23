from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import os
from pradip32767.settings import BASE_DIR
from . import views

urlpatterns = [
    path('',views.index,name='resume'),
] + static(os.path.join(BASE_DIR,'resume','static'), document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)