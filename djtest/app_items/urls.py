from django.urls import path, include
from rest_framework import routers
from app_items.views import ItemViewSet


router_item = routers.SimpleRouter()
router_item.register(r'item', ItemViewSet, basename='item')


urlpatterns = [
    path('', include(router_item.urls)),
]