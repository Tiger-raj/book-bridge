from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100)
    reg_no=models.BigIntegerField()
    year=models.IntegerField()
    age=models.IntegerField()
    email=models.CharField(max_length=50)
    passward=models.CharField(max_length=50)

class Book(models.Model):
    book_id=models.IntegerField
    book_name=models.CharField(max_length=100)
    book_available=models.BooleanField(default=True)

    
