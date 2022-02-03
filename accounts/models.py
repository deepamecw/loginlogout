from django.db import models


# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'reg_details'
    def __str__(self):
        return 'New user registered successfully....'
