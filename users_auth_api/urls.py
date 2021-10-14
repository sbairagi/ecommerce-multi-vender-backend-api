# from users_auth_api.models import DeliveryBoyProfile
from .views import DeliveryBoyViewSet, UserViewSet, SellerViewSet, UserProfileViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('sellerprofile', SellerViewSet)
router.register('deliveryboyprofile', DeliveryBoyViewSet)
router.register('userprofile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]