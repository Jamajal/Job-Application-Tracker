
from django.contrib import admin
from django.urls import path, re_path
from .views import login, signup, test_token, read_users, put_detail_delete_user, login_google, update_not_first_time, get_user_classgroups

urlpatterns = [
    path('api/v1/users/', read_users),
    path('api/v1/users/<int:pk>', put_detail_delete_user),
    #path('api/v1/users/registration/', UserCreate.as_view()),
    re_path('api/v1/auth/login', login),
    re_path('api/v1/signup', signup),
    re_path('api/v1/test_token', test_token),
]