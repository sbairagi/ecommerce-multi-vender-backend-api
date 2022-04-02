# from .views import DeliveryBoyViewSet, UserViewSet, SellerViewSet, UserProfileViewSet
from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('products', ProductsViewset)
# router.register('productdetail', ProductDetailViewSet)
# router.register('deliveryboy', DeliveryBoyViewSet)
# router.register('userprofiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]