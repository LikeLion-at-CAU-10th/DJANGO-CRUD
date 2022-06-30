from django.db import models

# Create your models here.
class Category(models.Model):
    # id = 자동 생성!!
    title = models.CharField(max_length=50, default= "메롱", null=True, blank=True) # null vs ''
    view_auth = models.IntegerField(default = 0,  null=True, blank=True)
    color = models.CharField(max_length=20, default="#808080",  null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)


# 힌트
# class Profile(models.Model):
#     name = 
#     age = 
#     phone = 
