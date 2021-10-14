# from crum import get_current_user
from PIL import Image
from django.core import mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField




class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=10)
    is_seller = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_delivery_boy = models.BooleanField(default=False)
    aproved_seller = models.BooleanField(default=False, max_length=6)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = "App User"
        verbose_name_plural = "App Users"

@receiver(post_save, sender=User, dispatch_uid="user_registration_notification")
def notify_new_user_registration(sender, created, instance, **kwargs):
    if created:
        try:
            subject = 'New user registration on {}'.format('MDS Cart India Online')
            html_message = render_to_string(
                'admin-notifications/new-user-registration-notification.html',
                {
                     'account_type': 'New User Registered',
                     'app_source': 'MDS Cart India Online',
                     'email': instance.email,
                     'first_name': instance.first_name,
                     'last_name': instance.last_name,
                     'phone_number': instance.phone_number
                }
            )
            plain_message = strip_tags(html_message)
            from_email = '{} <no-reply@appadminpanel.in>'.format('MDS Cart India Online')
            to = 'mdscart.noreplay@gmail.com'
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        except Exception as e:
            print(e)
            pass

SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
STATE_CHOICES = (
    ("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
    ("Andhra Pradesh",'Andhra Pradesh'),
    ("Arunachal Pradesh",'Arunachal Pradesh'),
    ("Assam",'Assam'),
    ("Bihar",'Bihar'),
    ("Chandigarh",'Chandigarh'),
    ("Chhattisgarh",'Chhattisgarh'),
    ("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
    ("Daman and Diu",'Daman and Diu'),
    ("Delhi",'Delhi'),
    ("Goa",'Goa'),
    ("Gujarat",'Gujarat'),
    ("Haryana",'Haryana'),
    ("Himachal Pradesh",'Himachal Pradesh'),
    ("Jammu & Kashmir",'Jammu & Kashmir'),
    ("Jharkhand",'Jharkhand'),
    ("Karnataka",'Karnataka'),
    ("Kerala",'Kerala'),
    ("Lakshadweep",'Lakshadweep'),
    ("Madhya Pradesh",'Madhya Pradesh'),
    ("Maharashtra",'Maharashtra'),
    ("Manipur",'Manipur'),
    ("Meghalaya",'Meghalaya'),
    ("Mizoram",'Mizoram'),
    ("Nagaland",'Nagaland'),
    ("Odisha",'Odisha'),
    ("Puducherry",'Puducherry'),
    ("Punjab",'Punjab'),
    ("Rajasthan",'Rajasthan'),
    ("Sikkim",'Sikkim'),
    ("Tamil Nadu",'Tamil Nadu'),
    ("Telangana",'Telangana'),
    ("Tripura",'Tripura'),
    ("Uttarakhand",'Uttarakhand'),
    ("Uttar Pradesh",'Uttar Pradesh'),
    ("West Bengal",'West Bengal'),
    )

class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='userprofile', primary_key=True)
    # customer_id = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(upload_to='user_photos', null=True)
    phone_number = models.CharField(max_length=10,null=True)
    alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(null=True)
    pincode = models.CharField(max_length=6, null=True)
    landmark = models.CharField(max_length=500, null=True, blank=True)
    locality = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
    sex = models.CharField(max_length=6,choices=SEX_CHOICES, null=True)
        

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.photo.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)


# @receiver(post_save, sender=UserProfile, dispatch_uid="user_registration_notification")
# def notify_new_user_registration(sender, created, instance, **kwargs):
#     if created:
#         try:
#             subject = 'New user registration on app {}'.format('MDS Cart India Online')
#             html_message = render_to_string(
#                 'admin-notifications/new-user-registration-notification.html',
#                 {
#                     'account_type': 'New Seller Registered',
#                     'app_source': 'MDSCART India Online',
#                     'email': instance.user.email,
#                     'first_name': instance.user.first_name,
#                     'last_name': instance.user.last_name,
#                     'phone_number': instance.phone_number
#                 }
#             )
#             plain_message = strip_tags(html_message)
#             from_email = '{} <no-reply@appadminpanel.in>'.format('MDS Cart India Online')
#             to = 'mdscart.noreplay@gmail.com'
#             mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
#         except Exception as e:
#             print(e)
#             pass

def get_image_path(instance, filename):
    return '{0}/{1}/{2}/{3}/{4}/{5}'.format('seller_Documents', instance.state, instance.city, instance.pincode,instance.user, filename)

class SallerDetail(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sellerprofile', primary_key=True)
	photo = models.ImageField(null=True,upload_to=get_image_path)
	adharcard = models.ImageField(null=True,upload_to=get_image_path)
	pancard = models.ImageField(null=True,upload_to=get_image_path)
	gumasta = models.ImageField(null=True,upload_to=get_image_path)
	phone_number = models.CharField(max_length=10,null=True)
	email = models.CharField(max_length=50, null=True)
	gst_Number = models.CharField(max_length=15,null=True)
	shop_Name = models.CharField(max_length=500,null=True)
	whatsapp_no = models.CharField(max_length=10,null=True)
	shop_Address = models.TextField(null=True)
	pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True)
	locality = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	account_Holder_Name = models.CharField(max_length=50, null=True)
	account_Number = models.CharField(max_length=20, null=True)
	ifsc_Code = models.CharField(max_length=11, null=True)
	bank_name = models.CharField(max_length=20, null=True)
	product_limite = models.CharField(default='25', max_length=3)
	seller_join_date = models.DateTimeField(auto_now_add=True, blank=True)


	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img = Image.open(self.photo.path)
	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.photo.path)
    

@receiver(post_save, sender=SallerDetail, dispatch_uid="seller_registration_notification")
def notify_new_seller_registration(sender, created, instance, **kwargs):
    if created:
        try:
            subject = 'New seller registration on {}'.format('MDSCART India Online')
            html_message = render_to_string(
                'admin-notifications/new-user-registration-notification.html',
                {
                    'account_type': 'New Seller Registered',
                    'app_source': 'MDSCART India Online',
                    'shop_name': instance.shop_Name,
                    'email': instance.user.email,
                    'first_name': instance.user.first_name,
                    'last_name': instance.user.last_name,
                    'phone_number': instance.phone_number
                 }
            )
            plain_message = strip_tags(html_message)
            from_email = '{} <no-reply@appadminpanel.in>'.format('MDSCART India Online')
            to = 'mdscart.noreplay@gmail.com'
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        except:
            pass

class DeliveryBoyProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='deliveryboyprofile', primary_key=True)
    adharcard = models.ImageField(null=True,upload_to='delivery_boy_adharcard')
    dob = models.DateField(null=True)
    photo = models.ImageField(null=True,upload_to='delivery_boy_photos')
    phone_number = models.CharField(max_length=10,null=True)
    alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(null=True)
    pincode = models.CharField(max_length=6, null=True)
    landmark = models.CharField(max_length=500, null=True, blank=True)
    locality = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
    sex = models.CharField(max_length=6,choices=SEX_CHOICES, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=DeliveryBoyProfile, dispatch_uid="delivery_boy_registration_notification")
def notify_new_Delivery_Boy_registration(sender, created, instance, **kwargs):
    if created:
        try:
            subject = 'New delivery boy registration on {}'.format('MDSCART India Online')
            html_message = render_to_string(
                'admin-notifications/new-user-registration-notification.html',
                {
                    'account_type': 'New Delivery Boy Registered',
                    'app_source': 'MDSCART India Online',
                    'email': instance.user.email,
                    'first_name': instance.user.first_name,
                    'last_name': instance.user.last_name,
                    'phone_number': instance.phone_number
                 }
            )
            plain_message = strip_tags(html_message)
            from_email = '{} <no-reply@appadminpanel.in>'.format('MDSCART India Online')
            to = 'mdscart.noreplay@gmail.com'
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        except:
            pass