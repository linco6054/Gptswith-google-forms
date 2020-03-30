from django.db import models
import datetime
from gforms.models import User , school

class period (models.Model):
    input_date=models.DateField(auto_now_add=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User,null=True, related_name='created_by',on_delete=models.SET_NULL)
    modified= models.BooleanField(default=True)
    modified_by = models.ForeignKey(User,null=True, related_name='modified_by',on_delete=models.SET_NULL)
    modified_date = models.DateField()
    is_active = models.BooleanField(default=False)
    
    
    
class category(models.Model):
    input_date=models.DateField(auto_now_add=True, editable=False)
    category_name = models.CharField(max_length=30)
    created_by = models.ForeignKey(User,null=True, related_name='made_by',on_delete=models.SET_NULL)
    
    category_secrate_key= models.CharField(max_length=100)
    google_form_link = models.TextField(default="null")
    category_description= models.TextField(default='Please answer all the questions in this category')
    category_status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_name

class champions (models.Model):
    input_date=models.DateField(auto_now_add=True, editable=False)
    year_won = models.DateField()
    category_won= models.ForeignKey(category, on_delete=models.CASCADE)
    school_won= models.ForeignKey(school, on_delete=models.CASCADE)
    
    
    
    