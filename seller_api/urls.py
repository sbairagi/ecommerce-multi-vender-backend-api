from .views import *
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('sellercart', SellerCartViewSet)
router.register('category', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('topsellerslider/', TopSellerSliderViewSet.as_view()),
    path('centersellerslider/', CenterSellerSliderViewSet.as_view()),
    path('bottomsellerslider/', BottomSellerSliderViewSet.as_view()),
    # path('category/', CategoryView.as_view()),
]