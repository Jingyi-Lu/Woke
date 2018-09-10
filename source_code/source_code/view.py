# -*- coding: utf-8 -*-

from django.shortcuts import render
 
def login(request):
    context          = {}
    return render(request, 'Login.html', context)

def successful(request):
    context          = {}
    return render(request, 'successful.html', context)