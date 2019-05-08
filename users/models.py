from django.db import models

# Create your models here.
class users(models.Model):
    code = models.CharField(max_length=20,null= True ,blank=True)
    name = models.CharField(max_length=10,null= True ,blank=True)
    sex = models.CharField(max_length=5 ,null= True ,blank=True)
    birthday = models.DateField(null= True ,blank=True)
    company_code = models.CharField(max_length=20,null= True ,blank=True)
    company_name = models.CharField(max_length=20,null= True ,blank=True)
    position = models.CharField(max_length=20 ,null= True ,blank=True)
    email = models.CharField(max_length=20 ,null= True ,blank=True)
    telephone = models.CharField(max_length=20 ,null= True ,blank=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
