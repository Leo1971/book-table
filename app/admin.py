# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import User
from app.models import Book

class Userlist(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ('id',)

class Booklist(admin.ModelAdmin):
    list_display = ('id','name','author')
    search_fields = ('id',)

# Register your models here.
admin.site.register(User, Userlist)
admin.site.register(Book, Booklist)