
from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer



class TopSellerSliderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = TopSellerSlider
        fields = ('name','image','category')
        read_only_fields = ('name','image','category')


class CenterSellerSliderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CenterSellerSlider
        fields = ['name','image','category']
        read_only_fields = ['name','image','category']

class BottomSellerSliderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = BottomSellerSlider
        fields = ['name','image','category']
        read_only_fields = ['name','image','category']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['root_category', 'sub_categories']

class CategorySerilaizer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['subcategory' , 'category', 'id']

        

# CategorySerilaizer.base_fields['subcategories'] = SubCategorySerializer()

    # def create(self, validated_data):
    #     # pass
    
    #     productsize = validated_data.pop('subcategories_set')
    #     # user = None
    #     # request = self.context.get("request")
    #     # if request and hasattr(request, "user"):
    #     #     user = request.user
    #     product = Category.objects.create(**validated_data)
    #     if len(productsize):
    #         for size in productsize:
    #             SubCategory.objects.create(product=product, **size)
    #     return product

    
        
class ProductSizeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['product_size_id','product', 'colour', 'size', 'quantity']
        read_only_fields = ['product']
        


class ProductReviewSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"



class ProductSerilaizer(WritableNestedModelSerializer,serializers.ModelSerializer):
    productsize = ProductSizeSerilaizer(many=True, required=False)
    product_review = ProductReviewSerilaizer(many=True, read_only=True)
    shop = serializers.HiddenField(read_only=False,write_only=True,default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['url','product_id','shop', 'product_name', 'category','root_category', 'subcategory', 'price', 'price_not', 'gst', 'desc', 'out_of_stock', 'pub_date', 'product_zipcode', 'quantity', 'image1', 'image2','image3', 'image4', 'image5', 'productsize', 'product_review']
        read_only_fields = ['out_of_stock']

        # def create(self, validated_data):
        #     productsize = validated_data.pop('productsize')
        #     # user = None
        #     # request = self.context.get("request")
        #     # if request and hasattr(request, "user"):
        #     #     user = request.user
        #     userid = validated_data.get('requestuser', validated_data.requestuser)
        #     product = Product.objects.create(shop=userid,**validated_data)
        #     if len(productsize):
        #         for size in productsize:
        #             ProductSize.objects.create(product=product, **size)
        #     return product

        # def update(self, instance, validated_data):
        #     productsize = validated_data.pop('productsize')
            # profile = instance.profile

            # instance.id = validated_data.get('id', validated_data.id)
            # instance.save()

            # if len(productsize):
            #     for size in productsize:
            #         ProductSize.objects.create(product=product, **size)
            # return product + " : " + productsize



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

            # return instance


class TrendingProductSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = TrendingProduct
        fields = "__all__"

class SellerCartSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = SellerCart
        fields = "__all__" 

class OrderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"