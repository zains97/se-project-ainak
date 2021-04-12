from django.db import models
from enum import IntEnum
from datetime import date
from datetime import datetime

# Create your models here.
class Home(models.Model):
    landscape1 = models.ImageField(upload_to="recommend_system/images", default="")
    landscape2 = models.ImageField(upload_to="recommend_system/images", default="")
    landscape3 = models.ImageField(upload_to="recommend_system/images", default="")
    category = models.CharField(max_length=20, default="")
    glassesname = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.glassesname

class User(models.Model):
    username = models.TextField(max_length=20, default="")
    fname = models.CharField(max_length=20, default="")
    lname = models.CharField(max_length=20, default="")
    email = models.TextField(max_length=20, default="")
    pass1 = models.TextField(max_length=20, default="")
    pass2 = models.TextField(max_length=20, default="")
    city = models.CharField(max_length=70)
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.TextField(max_length=20, default="")
    email = models.TextField(max_length=20, default="")
    pass1 = models.TextField(max_length=20, default="")

    def __str__(self):
        return self.username

class Search(models.Model):
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20)
    location = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    sft = models.IntegerField(default=0)
    email = models.CharField('User email', max_length=100)
    datetime = models.DateTimeField(default=datetime.now)

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

class Comment(models.Model):
    message = models.TextField('Message')
    rating = models.FloatField(default=0.0)
    time_comment = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)

class Contact_broker(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    email = models.CharField('User email', max_length=100)
    datetime = models.DateTimeField(default=datetime.now)

class Wish_list(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    email = models.CharField('User email', max_length=100)
    datetime = models.DateTimeField(default=datetime.now)

class Click_item(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    email = models.CharField('User email', max_length=100)
    datetime = models.DateTimeField(default=datetime.now)

class Buy(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    address = models.CharField(default="", max_length=100)
    reye = models.FloatField(default=0.0, null=True, blank=True)
    leye = models.FloatField(default=0.0, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.now)

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.email