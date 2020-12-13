
from django.conf.urls import url
from django.contrib import admin
from django.urls import (path, include)
from rest_framework.routers import DefaultRouter
from modules.core import views

routes = DefaultRouter()
routes.register('users', views.UserViewrSet)
routes.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(routes.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
