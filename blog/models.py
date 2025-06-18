from django.db import models
from django.utils.text import slugify
# Create your models here.

from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    img_url=models.ImageField(null=True,blank=True,upload_to='posts/images')
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)



    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title
