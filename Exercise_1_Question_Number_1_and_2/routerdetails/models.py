from django.db import models

# Create your models here.
class routerdeails(models.Model):
    sapid       =  models.CharField(max_length = 18)
    hostname    =  models.CharField(max_length = 14)
    loopback    =  models.CharField(max_length = 14)
    macadress   =  models.CharField(max_length = 17) 
    active_flag =  models.CharField(max_length = 1) 

    def __str__(self):
        return self.sapid