
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Credit(models.Model):
    cramounts=models.FloatField()
    crdates = models.DateField()
    deamounts=models.FloatField(default=0)
    crdescriptions = models.TextField()
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    

    def __str__(self):
        return self.crdescriptions

    def balance(self):
       items = Credit.objects.all()
       total=sum([item.deamounts for item in items])-sum([item.cramounts for item in items])
       return total
