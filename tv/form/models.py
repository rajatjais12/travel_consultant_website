from django.db import models
from django import forms
class log_in_m(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    email= models.EmailField(max_length=150, db_index=True)
    password = models.CharField(max_length=32,default="")
    def __str__(self):
     	return self.name


#class cstmr_d(models.Model):