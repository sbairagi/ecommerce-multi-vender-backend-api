from django.core import mail
from django.db.models import fields
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import DeliveryBoyProfile, SallerDetail, User, UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('url', 'dob', 'photo', 'phone_number', 'alternate_mobile', 'address', 'pincode', 'landmark', 'locality', 'city', 'state', 'sex')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        # user_data = User.objects.get(user=user)
        # print(user_data, user)
        user.is_user = True
        user.save()
        object = UserProfile.objects.create(user=user, **validated_data)
        return object


class SellerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SallerDetail
        fields = ('url', 'photo', 'adharcard', 'pancard', 'gumasta', 'phone_number', 'email', 'gst_Number', 'shop_Name', 'whatsapp_no', 'shop_Address', 'pincode', 'landmark', 'locality', 'city','state','account_Holder_Name', 'account_Number', 'ifsc_Code', 'bank_name')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user.is_seller = True
        user.save()
        object = SallerDetail.objects.create(user=user, **validated_data)
        return object

class DeliveryBoyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryBoyProfile
        fields = ('url', 'adharcard','dob','photo', 'phone_number','alternate_mobile','address','pincode', 'landmark', 'locality', 'city', 'state', 'sex')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        # user_data = User.objects.get(user=user)
        # print(user_data, user)
        user.is_delivery_boy = True
        user.save()
        object = DeliveryBoyProfile.objects.create(user=user, **validated_data)
        return object


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'email','phone_number', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = instance.get('phone_number', instance.phone_number)
        instance.save()

        # profile.dob = profile_data.get('dob', profile.dob)
        # profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        # profile.photo = profile_data.get('photo', profile.photo)
        # profile.alternate_mobile = profile_data.get('alternate_mobile', profile.alternate_mobile)
        # profile.address = profile_data.get('address', profile.address)
        # profile.pincode = profile_data.get('pincode', profile.pincode)
        # profile.landmark = profile_data.get('landmark', profile.landmark)
        # profile.locality = profile_data.get('locality', profile.locality)
        # profile.city = profile_data.get('city', profile.city)
        # profile.state = profile_data.get('state', profile.state)
        # profile.sex = profile_data.get('locality', profile.sex)
        # profile.save()

        return instance

