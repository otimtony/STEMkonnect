# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import authentication, permissions, serializers, viewsets, status, generics, parsers, renderers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import View, APIView
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class LoginUser(APIView):
    '''login user option'''
    content = {}
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.BasicAuthentication
    )
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        try:
            token, created = Token.objects.get_or_create(
                user=self.request.user
            )
            content = {
                'auth': unicode(token.key),
            }
        except Exception:
            pass
        return Response(content)



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer