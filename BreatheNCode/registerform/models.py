from django.db import models

class Userdetail(models.Model):
    first_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    user_email=models.EmailField()
    user_password=models.CharField(max_length=50)

class Userfulldetail(models.Model):
    first_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    user_email=models.EmailField()
    user_password=models.CharField(max_length=50)
    user_year=models.IntegerField()
    user_course=models.CharField(max_length=50)
    user_phone=models.CharField(max_length=20)
    user_reg_no=models.CharField(max_length=20)
    user_gender=models.CharField(max_length=1)







# Create your models here.
