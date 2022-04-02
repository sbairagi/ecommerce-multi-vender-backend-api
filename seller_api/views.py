from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from users_auth_api.models import SallerDetail
from .permissions import IsLoggedInUserOrAdmin, IsSellerOrApprovedUser
from .models import *
from .serializers import *
# Create your views here.
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TopSellerSliderViewSet(generics.ListAPIView):
    queryset = TopSellerSlider.objects.all()
    serializer_class = TopSellerSliderSerilaizer
    permission_classes = [AllowAny]


class CenterSellerSliderViewSet(generics.ListAPIView):
    queryset = CenterSellerSlider.objects.all()
    serializer_class = CenterSellerSliderSerilaizer
    permission_classes = [AllowAny]

class BottomSellerSliderViewSet(generics.ListAPIView):
    queryset = BottomSellerSlider.objects.all()
    serializer_class = BottomSellerSliderSerilaizer
    permission_classes = [AllowAny]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer
    permission_classes = [AllowAny]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
        

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer
    pagination_class= StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'list':
            query_set = queryset.filter(shop=self.request.user)
        elif self.action == 'retrieve':
            query_set = queryset.all()
        return query_set

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsSellerOrApprovedUser, IsAuthenticated]
        elif self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]



class SellerCartViewSet(viewsets.ModelViewSet):
    queryset = SellerCart.objects.all()
    serializer_class = SellerCartSerilaizer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsSellerOrApprovedUser, IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsSellerOrApprovedUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]