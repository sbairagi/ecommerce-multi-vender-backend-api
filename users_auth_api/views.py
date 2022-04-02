from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .permissions import IsLoggedInUserOrAdmin
from .models import User, SallerDetail, UserProfile, DeliveryBoyProfile
from datetime import datetime, timedelta
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser

# Create your views here.
from .serializers import UserProfileSerializer, SellerProfileSerializer, DeliveryBoyProfileSerializer, UserSerializer, UserProfileSerializer
import requests


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(email=self.request.user.email)
        return query_set

    # Permissions
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class DeliveryBoyViewSet(viewsets.ModelViewSet):
    queryset = DeliveryBoyProfile.objects.all()
    serializer_class = DeliveryBoyProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class SellerViewSet(viewsets.ModelViewSet):
    queryset = SallerDetail.objects.all()
    serializer_class = SellerProfileSerializer
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    # parser_class = 


    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user.id)
        return query_set

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]