from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:GPIO_Pin>/', views.detail, name='detail'),
    path('api/', views.index_json, name='index_json'),
    path('api/<int:GPIO_Pin>/', views.detail_json, name='detail_json'),
]