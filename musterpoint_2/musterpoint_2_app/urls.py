from django.urls import path
from . import views

app_name = 'musterpoint_2_app'
urlpatterns = [
    path('', views.index, name='index')
]
