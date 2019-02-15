from django.urls import path

from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:GPIO_Pin>/', views.detail, name='detail'),
    path('api/', views.index_json, name='index_json'),
    path('api/<int:GPIO_Pin>/', views.detail_json, name='detail_json'),
    path('<int:GPIO_Pin>/toggle/', views.toggle, name='toggle'),
]