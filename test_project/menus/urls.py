from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:pk>/', views.main, name='main_pk')
]   