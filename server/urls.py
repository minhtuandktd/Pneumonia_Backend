from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve

from PneumoniaApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # new 
    path("pneumonia/", views.call_model.as_view()),
]
