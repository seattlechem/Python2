# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    try:
        request.session['submissiontimes']
    
    except:
        request.session['submissiontimes'] = 0

    return render(request, 'surveys/index.html')

def process(request):
    request.session['name'] = request.POST['Name']
    request.session['location'] = request.POST['location']
    request.session['favlanguage'] = request.POST['favlanguage']
    request.session['comment'] = request.POST['comment']

    request.session['submissiontimes'] += 1

    return redirect('/result')

def result(request):
    context = {
        "submissiontimes": request.session['submissiontimes'],
        "fname": request.session['name'],
        "flocation": request.session['location'],
        "ffavlanguage": request.session['favlanguage'],
        "fcomment": request.session['comment']
    }
    
    return render(request, 'surveys/result.html', context)