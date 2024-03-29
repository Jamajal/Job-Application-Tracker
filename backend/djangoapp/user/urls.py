
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView, signup, read_users, read_update_delete_user

urlpatterns = [
    path('api/v1/user/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/user/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/user/signup', signup, name='Signup'),
    path('api/v1/users', read_users, name='Get users'),
    path('api/v1/users/<int:pk>', read_update_delete_user, name='Get/Patch/Delete user'),
]