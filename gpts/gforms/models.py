from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django import template
# Create your models here.
register = template.Library()
#users management class


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    # this is what i had in mind
    is_normal_user=models.BooleanField('Normal Staff', default=False)
    is_school_admin=models.BooleanField('Shool Admin', default=False)
    is_system_admin=models.BooleanField('system admin', default=False)
    is_desable_user=models.BooleanField('suspendes School Admin ', default=False)
    
    def __str__(self):
        return self.username


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'


@register.filter(name='has_group')
def has_group(user, group_name):
    # group = Group.objects.get(name=group_name)
    # return True if group in user.groups.all() else False
    return user.groups.filter(name=group_name).exists()

class school(models.Model):
    input_date=models.DateField(auto_now_add=True, editable=False)
    school_name= models.CharField(max_length=100)
    school_mail= models.EmailField(max_length=256)
    school_phone_number= models.PositiveIntegerField()
    county=models.CharField(max_length=100)
    sub_county =models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    school_website_link = models.CharField(max_length=300)
    school_admin=models.ForeignKey(User, on_delete=models.CASCADE)
    school_status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.school_name