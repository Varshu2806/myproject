
from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserProfileView,
    UserListView,
    SendOTPView,
    

)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
]
