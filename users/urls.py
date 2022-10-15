from django.urls import path
from .views import RegistrationView, LoginView, StatusView
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('status/', StatusView.as_view()),
]