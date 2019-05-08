from django.db import models

# Create your models here.
class types(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

class lists(models.Model):
    name = models.CharField(max_length=20,null= True , blank= True)
    address = models.CharField(max_length=20,null= True , blank= True)
    company_code = models.CharField(max_length=20,null= True , blank= True)
    company_name = models.CharField(max_length=20,null= True , blank= True)
    type_code = models.CharField(max_length=10,null= True , blank= True)
    type_name = models.CharField(max_length=20,null= True , blank= True)
    date = models.DateField(null= True , blank= True)
    description = models.CharField(max_length=500,null= True , blank= True)