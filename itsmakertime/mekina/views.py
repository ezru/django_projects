#from django.shortcuts import render #This import come with the original file

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Meet Mekina. The world's first fully 3D printable buggy robot!")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of queston %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)