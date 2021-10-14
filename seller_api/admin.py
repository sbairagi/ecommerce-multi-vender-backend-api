from django.contrib import admin
from django.db.models.base import Model
from .models import *
# Register your models here.

class ProductReviewAdmin(admin.StackedInline):
    model = ProductReview

class ProductSizeAdmin(admin.StackedInline):
    model = ProductSize

class SubCategoryAdmin(admin.StackedInline):
    model = SubCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductReviewAdmin,ProductSizeAdmin)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    # model = Category
    inlines = (SubCategoryAdmin, )

admin.site.register((ProductSize,))