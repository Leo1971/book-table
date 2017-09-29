# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Book
from django.http import HttpResponse

def list(request):
    list = Book.objects.all()
    context = {"list": list}
    return render(request, 'index.html', context)

def insert(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        author = request.POST['author']
        try:
            newitem = Book(id = id, name = name, author = author)
            newitem.save()
        except:
            print "insert error"
    # newitem = Book(id = '9',name = 'd', author = 'keke')
    # newitem.save()
    list = Book.objects.all()
    context = {"list": list}
    return render(request, 'index.html', context)

def delete(request):
    if request.method == "POST":
        id = request.POST['did']
    item = Book.objects.get(id = id)
    item.delete()
    list = Book.objects.all()
    context = {"list": list}
    return render(request, 'index.html', context)

def search(request):
    if request.method == "GET":
        id = request.GET['sid']
        if id == '':
            newlist = Book.objects.all()
        else:
            try:
                newlist = Book.objects.filter(id=id)
            except:
                newlist = None
                print "this book doesn't exist."

        context = {"list": newlist}
        return render(request, 'index.html', context)
