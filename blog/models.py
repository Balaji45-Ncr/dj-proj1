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

    @property
    def formatted_img_url(self):
        if self.img_url and str(self.img_url).startswith(('http://', 'https://')):
            return str(self.img_url)
        elif self.img_url and hasattr(self.img_url, 'url'):
            return self.img_url.url
        return 'ChatGPT_Image_May_4_2025_02_09_02_PM.png'  # or some default image URL

    def __str__(self):
        return self.title
