from rest_framework import serializers

from seller_api.models import Product, ProductReview, ProductSize



class HomeProductsSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['url','product_name','price','price_not','image1']


# class ProductSizedetailSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductSize
#         fields = ['product_size_id','product', 'colour', 'size', 'quantity']
#         read_only_fields = ['product']
        


# class ProductReviewDetailSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductReview
#         fields = "__all__"



# class ProductDetailSerilaizer(serializers.ModelSerializer):
#     productsize = ProductSizedetailSerilaizer(many=True, read_only=True)
#     product_review = ProductReviewDetailSerilaizer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = ['shop', 'product_name', 'category','root_category', 'subcategory', 'price', 'price_not','desc', 'out_of_stock','product_zipcode', 'quantity', 'image1', 'image2','image3', 'image4','productsize', 'product_review']
#         read_only_fields = ['out_of_stock']
