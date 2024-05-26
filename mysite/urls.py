from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movies_router') 
router.register('action', ActionViewSet, basename='action_router')
router.register('comedy', ComedyViewSet, basename='comedy_router') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
