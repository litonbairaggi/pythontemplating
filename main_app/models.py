from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=700,blank=False)
    blog_img = models.ImageField(upload_to='blog/',blank=False)

class Gallery(models.Model):
    name = models.CharField(max_length=100,blank=False)
    gallery_img = models.ImageField(upload_to='gallery/',blank=False)

class Teams(models.Model):
    name = models.CharField(max_length=100,blank=False)
    designation = models.TextField(max_length=700,blank=False)
    facebook = models.CharField(max_length=50,blank=False)
    linkedin = models.CharField(max_length=50,blank=False)
    twitter = models.CharField(max_length=50,blank=False)
    instagram = models.CharField(max_length=50,blank=False)
    team_img= models.ImageField(upload_to='teams/',blank=False)

class Services(models.Model):
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    services_img = models.ImageField(upload_to='services/',blank=False)

class Testimoinials(models.Model):
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    testimoinial_img = models.ImageField(upload_to='testimoinials/',blank=False)

class Setting(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)
    phome = models.CharField(max_length=100,blank=False)
    facebook = models.CharField(max_length=100,blank=False)
    linkedin = models.CharField(max_length=100,blank=False)
    twitter = models.CharField(max_length=100,blank=False)
    instagram = models.CharField(max_length=100,blank=False)
    company_address = models.CharField(max_length=100,blank=False)
    logo_img = models.ImageField(upload_to='settings/',blank=False)

    def save(self):
        # count will have all of the objects from the Seeting model
        count = Setting.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = Setting.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(Setting, self).save()
        elif save_permission:
            super(Setting, self).save()

    def has_add_permission(self):
        return Setting.objects.filter(id=self.id).exists()

class Slider(models.Model):
    name = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    sliders_img = models.ImageField(upload_to='sliders/',blank=False)
