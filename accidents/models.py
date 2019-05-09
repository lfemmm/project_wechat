from django.db import models

# Create your models here.
# class accidentManager(models.Manager):
#     def add_accident(self, name, address, company_code, company_name, item, type_code, type_name, rank_code, rank_name,
#                      date, description):
#         accident = lists()
#         accident.name = name
#         accident.address = address
#         accident.company_code = company_code
#         accident.company_name = company_name
#         accident.item = item
#         accident.type_code = type_code
#         accident.type_name = type_name
#         accident.rank_code = rank_code
#         accident.rank_name = rank_name
#         accident.date = date
#         accident.description = description
#         accident.save()

class rank1(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

class type1(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

class list1(models.Model):
    name = models.CharField(max_length=20,null= True , blank= True)
    address = models.CharField(max_length=20,null= True , blank= True)
    company_code = models.CharField(max_length=20,null= True , blank= True)
    company_name = models.CharField(max_length=20,null= True , blank= True)
    item = models.CharField(max_length=20,null= True , blank= True)
    type_code = models.CharField(max_length=10,null= True , blank= True)
    type_name = models.CharField(max_length=20,null= True , blank= True)
    rank_code = models.CharField(max_length=10,null= True , blank= True)
    rank_name = models.CharField(max_length=20,null= True , blank= True)
    date = models.DateField(null= True , blank= True)
    description = models.CharField(max_length=500,null= True , blank= True)



