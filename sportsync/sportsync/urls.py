from django.contrib import admin
from django.urls import path, include
from sportsync_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
]
