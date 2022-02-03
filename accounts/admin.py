from django.contrib import admin

from accounts.views import register
from . models import register 

# Register your models here.
class userreg(admin.ModelAdmin):
    user_details = ['username','email']



admin.site.register(register)