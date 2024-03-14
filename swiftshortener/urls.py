from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original')
]