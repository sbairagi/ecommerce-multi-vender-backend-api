from django.db import models
from PIL import Image

from users_auth_api.models import User

# Create your models here.
class TopSellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	category = models.CharField(max_length=50, default = "#", null=True)

	def __str__(self):
		return str(self.name)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img = Image.open(self.image.path)
	# 	if img.height > 1024 or img.width > 1024:
	# 		output_size = (1024, 1024)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)

class CenterSellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	category = models.CharField(max_length=50, default = "#", null=True)

	def __str__(self):
		return str(self.name)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img = Image.open(self.image.path)
	# 	if img.height > 1024 or img.width > 1024:
	# 		output_size = (1024, 1024)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)

class BottomSellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	category = models.CharField(max_length=50, default = "#", null=True)

	def __str__(self):
		return str(self.name)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img = Image.open(self.image.path)
	# 	if img.height > 1024 or img.width > 1024:
	# 		output_size = (1024, 1024)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=50, default="")

	def __str__(self):
		return str(self.category)

class SubCategory(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,  related_name='subcategory', on_delete=models.CASCADE)
	root_category  = models.CharField(default="", max_length=25)
	sub_categories  = models.TextField(default="", help_text="add multiple items seprated by ','commas")

	# def __str__(self):
	# 	return str(self.category) + str(self.sub_Categories)


class Product(models.Model):
	GST_CHOICES = (("0",'0'),("3",'3'),("5",'5'),("12",'12'),("18",'18'),("28",'28'))
	outOfStock = (("False",'False'),("True",'True'))
	product_id = models.BigAutoField(primary_key=True)
	shop = models.ForeignKey(User, on_delete=models.CASCADE,default='')
	product_name = models.CharField(max_length=100)
	category = models.CharField(max_length=50,default="")
	root_category = models.CharField(max_length=50, default="")
	subcategory = models.CharField(max_length=50, default="")
	price = models.PositiveIntegerField(default=0)
	price_not = models.PositiveIntegerField(default=999)
	desc = models.TextField()
	gst = models.CharField(default='0',max_length=3,choices=GST_CHOICES)
	pub_date = models.DateField(auto_now=True)
	aproved_product = models.BooleanField(max_length=5, default=False)
	product_zipcode = models.CharField(max_length=10)
	out_of_stock = models.CharField(default='False', choices=outOfStock, help_text="True this field to Show Product is Out Of Stock" ,max_length=6)
	quantity = models.IntegerField(default=1, null=True, blank=True)
	image1 = models.ImageField(upload_to='products/images', default="")
	image2 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image3 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image4 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image5 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img1 = Image.open(self.image1)
	# 	if img1.height > 1500 or img1.width > 1500:
	# 		output_size = (1500, 1500)
	# 		img1.thumbnail(output_size)
	# 		img1.save(self.image1)

	# 	if self.image2:
	# 		img2 = Image.open(self.image2.path)
	# 		if img2.height > 1500 or img2.width > 1500:
	# 			output_size = (1500, 1500)
	# 			img2.thumbnail(output_size)
	# 			img2.save(self.image2.path)

	# 	if self.image3:
	# 		img3 = Image.open(self.image3.path)
	# 		if img3.height > 1500 or img3.width > 1500:
	# 			output_size = (1500, 1500)
	# 			img3.thumbnail(output_size)
	# 			img3.save(self.image3.path)

	# 	if self.image4:
	# 		img4 = Image.open(self.image4.path)
	# 		if img4.height > 1500 or img4.width > 1500:
	# 			output_size = (1500, 1500)
	# 			img4.thumbnail(output_size)
	# 			img4.save(self.image4.path)

	# 	if self.image5:
	# 		img5 = Image.open(self.image5.path)
	# 		if img5.height > 1500 or img5.width > 1500:
	# 			output_size = (1500, 1500)
	# 			img5.thumbnail(output_size)
	# 			img5.save(self.image5.path)

	def __str__(self):
		return str(self.product_name)

class ProductSize(models.Model):
	product_size_id = models.BigAutoField(primary_key=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='productsize')
	colour = models.CharField(max_length=50, null=True, blank=True)
	

class ProductSize_and_quantity(models.Model):
	id = models.BigAutoField(primary_key=True)
	productsize = models.ForeignKey(ProductSize,on_delete=models.CASCADE, related_name='productsize_and_quantity')
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	size = models.CharField(max_length=20, null=True, blank=True)
	quantity = models.IntegerField(default=0)

	# def __str__(self):
	# 	return str(self.product_size_id)

	
class ProductReview(models.Model):
	product_review_id = models.BigAutoField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
	shop = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.TextField()
	time = models.DateTimeField(auto_now=True)
	product_rating = models.PositiveIntegerField()

	# def __str__(self):
	# 	return str(self.product_review_id)

class TrendingProduct(models.Model):
	outofstock = ((False,False),(True,True))
	tranding_product_id = models.BigAutoField(primary_key=True)
	product = models.OneToOneField(Product, default="", on_delete=models.CASCADE)
	number = models.PositiveIntegerField()
	out_of_stock = models.BooleanField(default=False, choices=outofstock, help_text="True this field to Show Product is Out Of Stock",max_length=6)
	
	def __str__(self):
		return str(self.product)

class SellerCart(models.Model):
	seller_cart_id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.CharField(max_length=100)
	number = models.PositiveIntegerField(default=0)

	def __str__(self):
		return str(self.user)

class Order(models.Model):
	STATUS_CHOICES = (("Accepted",'Accepted'),("Packed",'Packed'),("On The Way",'On The Way'),("Delivered",'Delivered'),("Return",'Return'),("Cancel",'Cancel'))
	PAYMENT_METHOD = (("Online",'Online'),("CashOnDelivery",'CashOnDelivery'))
	order_id = models.CharField(max_length=50,default='')
	saler = models.CharField(max_length=100,default='wrappers@admin',)
	user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
	product_id = models.CharField(max_length=50)
	product_name = models.CharField(max_length=220)
	price = models.CharField(max_length=50)
	product_cat_subcat = models.CharField(max_length=220,null=True)
	size = models.CharField(max_length=50,default='',null=True, blank=True)
	quantity = models.IntegerField(default=1)
	status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='')
	deliver_boy_number = models.CharField(max_length=15,null=True)
	order_date_time = models.DateTimeField(auto_now=True)
	payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD, default='CashOnDelivery')