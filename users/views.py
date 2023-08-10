from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from . import serializers
# Create your views here.

class UserDetailsAPI(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    model = User

    def get_object(self):
        return self.request.user