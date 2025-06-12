from django.contrib import admin
from .models import Post,Category
# Register your models here.


class Postadmin(admin.ModelAdmin):
    list_display = ['title','content','created_at']
    list_filter = ['title','created_at','category']
    search_fields = ['title']

admin.site.register(Post,Postadmin)
admin.site.register(Category)