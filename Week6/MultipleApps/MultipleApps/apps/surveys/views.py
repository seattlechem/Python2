# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to display all surveys created")

def new(request):
    return HttpResponse("placeholder for users to add a new survey")
    
def create(request):
    return redirect('/surveys')

def show(request, survey_id):
    return HttpResponse("placeholder to display survey {}".format(survey_id))

def edit(request, survey_id):
    return HttpResponse("placeholder to edit survey {}".format(survey_id))
    
def delete(request, survey_id):
    return redirect('/surveys')
