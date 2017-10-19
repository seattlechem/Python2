# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



# Create your views here.

# index
def index(request):
    try:
        request.session['attempt']

    except KeyError:
        request.session['attempt'] = 0

    #return HttpResponse("hello")
    return render(request, "random_word/index.html")

def generate(request):
    request.session['attempt'] += 1
    request.session['random_word'] = get_random_string(length=8)
    return redirect('/random_word')

def reset(request):
    del request.session['attempt']
    del request.session['random_word']
    return redirect('/random_word')