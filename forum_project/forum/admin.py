from django.contrib import admin

from django.contrib import admin
from .models import Category, Thread, Reply


admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Reply)