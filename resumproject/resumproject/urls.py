
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('home/', views.home),
    path('contact/', views.contact),
    path('soo/', include('serv.urls')),



]
