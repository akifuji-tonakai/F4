from django.contrib import admin

from .models import Content, Chara, PostTwi
# Register your models here.

admin.site.register((Content, Chara, PostTwi))
