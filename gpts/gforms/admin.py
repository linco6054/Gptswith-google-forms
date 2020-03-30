from django.contrib import admin
from . models import User, school , profile 
from front.models import champions
# Register your models here.
admin.site.register(User)
admin.site.register(school)
admin.site.register(profile)
admin.site.register(champions)
