import jwt
from django.contrib.auth.models import User
from django.http import HttpRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import UserSerializer, LoginSerializer, UserGUDSerializer, \
    UserGUDSerializerOne, UserSerializerOutput
from django.contrib import auth
from django.core.cache import cache


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={201: UserSerializerOutput})
    def post(self, request: HttpRequest) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    @swagger_auto_schema(responses={201: '{"token": string}'})
    def post(self, request: HttpRequest) -> Response:
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, 'secret', algorithm='HS256')

            data = {'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED)


class UserGUD(ListModelMixin, GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserGUDSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        return self.list(request, *args, *kwargs)


class UserGUDUsername(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserGUDSerializerOne
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'

    def delete(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            username = request.data.get('username', None)
            response = super().delete(request, *args, **kwargs)

            if response.status_code == 204:
                cache.delete('{}'.format(username))
                return response

        except Exception:
            return Response({'Message': 'Not found user with this name'})

    def update(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            response = super().update(request, *args, **kwargs)

            if response.status_code == 200:
                mydata = response.data

                cache.set('username: {}'.format(mydata.get('username', None)),
                          {
                    'username': mydata['username'],
                    'password': mydata['password'],
                    'first_name': mydata['first_name'],
                    'last_name': mydata['last_name'],
                    'email': mydata['email'],
                    'is_active': mydata['is_active']
                })

                return response

        except Exception:
            return Response({'Message': 'Not found user with this name'})

    def patch(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            response = super().update(request, *args, **kwargs)

            if response.status_code == 200:
                mydata = response.data

                cache.set('username: {}'.format(mydata.get('username', None)),
                          {
                    'username': mydata['username'],
                    'first_name': mydata['first_name'],
                    'last_name': mydata['last_name'],
                    'email': mydata['email'],
                    'is_active': mydata['is_active']
                })

                return Response({'Message': 'Update'})

        except Exception:
            return Response({'Message': 'Not found user with this name'})


class UserGUDid(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserGUDSerializerOne
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def delete(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            id = request.data.get('id', None)
            response = super().delete(request, *args, **kwargs)

            if response.status_code == 204:
                cache.delete('{}'.format(id))
                return response

        except Exception:
            return Response({'Message': 'Not found user with this id'})

    def update(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            response = super().update(request, *args, **kwargs)

            if response.status_code == 200:
                mydata = response.data

                cache.set('id: {}'.format(mydata.get('id', None)),
                          {
                    'username': mydata['username'],
                    'first_name': mydata['first_name'],
                    'last_name': mydata['last_name'],
                    'email': mydata['email'],
                    'is_active': mydata['is_active']
                })

                return response

        except Exception:
            return Response({'Message': 'Not found user with this id'})

    def patch(self, request: HttpRequest, *args, **kwargs) -> Response:
        try:
            response = super().update(request, *args, **kwargs)

            if response.status_code == 200:
                mydata = response.data

                cache.set('id: {}'.format(mydata.get('id', None)),
                          {
                    'username': mydata['username'],
                    'first_name': mydata['first_name'],
                    'last_name': mydata['last_name'],
                    'email': mydata['email'],
                    'is_active': mydata['is_active']
                })

                return response

        except Exception:
            return Response({'Message': 'Not found user with this id'})