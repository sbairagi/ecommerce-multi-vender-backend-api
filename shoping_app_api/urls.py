
from django.contrib import admin
from django.urls import path, include
from .reset_password_view.views import PasswordResetConfirmView, PasswordResetView
from notificationsapi.views import FCMDeviceAuthorizedViewSet
from django.contrib.auth import views as auth_view

admin.site.site_header = "Shopping App Admin Portal"
admin.site.site_title = "Shopping App Admin Portal"
admin.site.index_title = "Welcome to Shopping App Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users_auth_api.urls')),
    path('api/notifications/', include('notificationsapi.urls')),
    path('userapi/', include('user_api.urls')),
    path('sellerapi/', include('seller_api.urls')),
    path('wholesaleapi/', include('wholesale_api.urls')),

    #third party api
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}),
         name='create_fcm_device'),

    #Auth Urls
    path('auth/password/reset/', PasswordResetView.as_view(),
        name='rest_password_reset'),
    path('auth/', include('rest_auth.urls')),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
