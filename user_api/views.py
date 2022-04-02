from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from seller_api.models import Product
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from user_api.serializers import HomeProductsSerilaizer

from users_auth_api.permissions import IsAdminUser, IsLoggedInUserOrAdmin

# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000



class ProductsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = HomeProductsSerilaizer
    pagination_class= StandardResultsSetPagination

    @action(methods=["get"], detail=False, url_path="filterProducts", url_name="filterProducts")
    def filterByCategoryRootcategorySubcategory(self, request, *args, **kwargs):
        category = self.request.query_params.get('category', '')
        rootcategory = self.request.query_params.get('rootcategory', '')
        subcategory = self.request.query_params.get('subcategory', '')
        if rootcategory =='' and subcategory=='':
            queryset = Product.objects.filter(category=category)
        elif subcategory=='':
            queryset = Product.objects.filter(category=category, root_category=rootcategory) #.order_by('-rating')
        else:
            queryset = Product.objects.filter(category=category, root_category=rootcategory,subcategory=subcategory)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


# class ProductDetailViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerilaizer
#     permission_classes = [AllowAny]

#     def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         elif self.action == 'retrieve' or self.action == 'list':
#             permission_classes = []
#         return [permission() for permission in permission_classes]