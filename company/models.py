from django.db import models

# Create your models here.
class company(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    parentID = models.ForeignKey('self' , null= True , blank= True ,on_delete = models.CASCADE)
    description = models.CharField(max_length=200 ,null=True ,blank=True)
    def __str__(self):
        return (self.code+self.name)
