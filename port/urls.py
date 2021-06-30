from .import views
from django.urls import path

urlpatterns = [
    path('', views.portView, name='port'),
    path('home/', views.portView, name='port'),
    
]