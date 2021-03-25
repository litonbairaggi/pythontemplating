from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    blog_img = models.CharField(max_length=200)

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    gallery_img = models.CharField(max_length=200)

class Teams(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    team_img= models.CharField(max_length=200)

class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    services_img = models.CharField(max_length=200)
