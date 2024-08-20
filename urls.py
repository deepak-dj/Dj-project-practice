from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myApp import views

router = DefaultRouter()
router.register('persons', views.PersonViewSet, basename='persons')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
