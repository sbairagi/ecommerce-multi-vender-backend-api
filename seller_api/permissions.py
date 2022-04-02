from rest_framework import permissions

from users_auth_api.models import SallerDetail, User, UserProfile


class IsLoggedInUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

    def has_permission(self, request, view):
        return request.user or request.user.is_staff

class IsSellerOrApprovedUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            is_seller = User.objects.get(id=request.user.id).is_seller
        except:
            is_seller = False
        try:
            approved_seller = User.objects.get(id=request.id).aproved_seller
        except:
            approved_seller = False
        return is_seller and approved_seller

    def has_permission(self, request, view):
        try:
            is_seller = User.objects.get(id=request.user.id).is_seller
        except:
            is_seller = False
        try:
            approved_seller = User.objects.get(id=request.user.id).aproved_seller
        except:
            approved_seller = False
        return is_seller and approved_seller


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff