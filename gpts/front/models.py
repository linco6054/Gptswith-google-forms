from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class period (models.Model):
    input_date=models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User,null=True, related_name='created_by',on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User,null=True, related_name='modified_by',on_delete=models.SET_NULL)
    modified_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    
    

    