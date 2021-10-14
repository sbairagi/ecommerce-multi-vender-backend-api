from django.contrib import admin

from django.db.models import Q, fields
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.base import Model

from seller_api.models import SellerCart
from user_api.models import UserCart
from .models import User, UserProfile, SallerDetail, DeliveryBoyProfile
from django.utils.translation import ugettext_lazy as _
from django import forms



class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class SellerCartInline(admin.StackedInline):
    model = SellerCart

class UserCartInline(admin.StackedInline):
    model = UserCart

class SallerProfileInline(admin.StackedInline):
    model = SallerDetail
    can_delete = False

class DeliveryBoyProfileInline(admin.StackedInline):
    model = DeliveryBoyProfile
    can_delete = False

admin.site.register((UserProfile, DeliveryBoyProfile, SallerDetail))


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # form = Userfields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','is_user', 'is_seller', 'is_delivery_boy', 'aproved_seller')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # list_display = ('email', 'first_name', 'last_name', 'get_customer_id', 'get_phone_number', 'get_app_source', 'get_permissions', 'date_joined')
    # list_display_links = ('email', 'first_name', 'last_name', 'get_customer_id', 'get_phone_number', 'get_app_source')
    # search_fields = ('email', 'first_name', 'last_name', 'profile__customer_id', 'profile__phone_number', 'profile__app_source')
    readonly_fields = ('is_superuser', 'groups', 'user_permissions')
    # list_select_related = ('profile', )
    # ordering = ('-id',)
    inlines = (UserProfileInline, SallerProfileInline, DeliveryBoyProfileInline, SellerCartInline, UserCartInline)

    # def get_queryset(self, request):
    #     qs = super(UserAdmin, self).get_queryset(request)
    #     if request.user.profile.belongs_to == 'ifl_services':
    #         return qs.filter(Q(profile__belongs_to='ifl_services'))
    #     elif request.user.profile.belongs_to == 'EquityGlobal':
    #         return qs.filter(Q(profile__belongs_to='EquityGlobal'))

    # def get_customer_id(self, instance):
    #     return instance.profile.customer_id
    # get_customer_id.short_description = 'Customer ID'

    # def get_phone_number(self, instance):
    #     return instance.profile.phone_number
    # get_phone_number.short_description = 'Phone Number'

    # def get_app_source(self, instance):
    #     return instance.profile.app_source
    # get_app_source.short_description = 'App Source'

    # def get_permissions(self, instance):
    #     return instance.profile.permissions
    # get_permissions.short_description = 'Permissions'


# @admin.register(AppPricing)
# class AppPricingAdmin(admin.ModelAdmin):
#     search_fields = ['in_app_pricing',]
#     list_display = ['in_app_pricing',]
#     list_display_links = ['in_app_pricing',]
