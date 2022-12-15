from django.db import models



class userDataModel(models.Model):
    username = models.CharField(max_length=50,blank=False, null=False)
    name = models.CharField(max_length=100,blank=False, null=False)
    email = models.EmailField(max_length=100,blank=False, null=False)
    password = models.CharField(max_length=100,blank=False, null=False)
    phone = models.CharField(max_length=100,blank=False, null=False)
    

    def __str__(self):
        return self.name
