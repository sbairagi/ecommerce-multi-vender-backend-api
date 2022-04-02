from django.db import models

from users_auth_api.models import User

# Create your models here.
class TopUserSlider(models.Model):
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

class CenterUserSlider(models.Model):
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

class BottomUserSlider(models.Model):
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



class UserCart(models.Model):
	user_cart_id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.CharField(max_length=100)
	number = models.PositiveIntegerField(default=0)

	def __str__(self):
		return str(self.user)
		

class Contact(models.Model):
	date = models.DateField(auto_now=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	
	def __str__(self):
		return self.email