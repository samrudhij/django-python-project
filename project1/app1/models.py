from django.db import models

# Create your models here.
class Help(models.Model):
  myName=models.CharField(max_length=12)
  myEmail=models.CharField(max_length=12)
  msg=models.CharField(max_length=13)

class Login(models.Model):
   email=models.CharField(max_length=15,null=False)
   password=models.CharField(max_length=10)

class Feedback(models.Model):
   email=models.CharField(max_length=15,null=False)
   feedback=models.TextField()
class Product(models.Model):
   productId=models.IntegerField()
   productName=models.CharField(max_length=25)
   price=models.IntegerField()
   image=models.ImageField()


class Order(models.Model):
   orderid=models.IntegerField()
   productId=models.IntegerField()
   customer=models.CharField(max_length=25)
   isCancelled=models.BooleanField(default=False)




   



  