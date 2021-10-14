# from .views import DeliveryBoyViewSet, UserViewSet, SellerViewSet, UserProfileViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('seller', SellerViewSet)
# router.register('deliveryboy', DeliveryBoyViewSet)
# router.register('userprofiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]