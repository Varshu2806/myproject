from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path
@api_view(['GET'])
def api_root(request):
    return Response({
        "register": "/api/register/",
        "login": "/api/login/",
        "profile": "/api/profile/",
        "send-otp": "/api/send-otp/",
        "users": "/api/users/"
    })

from .views import (
    RegisterView,
    LoginView,
    UserProfileView,
    UserListView,
    SendOTPView,
)
urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
]
