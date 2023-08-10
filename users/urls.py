from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('login/', obtain_auth_token),
    path('', views.UserDetailsAPI.as_view())
]