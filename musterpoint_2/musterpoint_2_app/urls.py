from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

app_name = 'musterpoint_2_app'

router = DefaultRouter()

router.register('units', views.UnitDatasheetViewSet, basename='units'),
router.register('wargear', views.WargearViewSet, basename='wargear')
router.register('list', views.ListViewSet, basename='list')

urlpatterns = [
    path('', views.index, name='index')
] + router.urls
