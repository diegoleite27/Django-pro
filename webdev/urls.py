from django.urls import re_path, path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path(r'^$', views.show),
    path(r'^add/', views.add), ]