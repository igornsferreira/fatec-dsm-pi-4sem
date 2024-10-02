from django.contrib import admin
from django.urls import path, include
from sportsync_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('login-email/', views.LoginEmailView.as_view(), name='login-email'),
]
