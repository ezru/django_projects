#from django.shortcuts import render #This import come with the original file

from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {"latest_question_list": latest_question_list}
    return render(request, "mekina/index.html")

    #template = loader.get_template("mekina/index.html")
    #context = {
    #    "latest_question_list": latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

    #output = '<br> '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. Meet Mekina. The world's first fully 3D printable buggy robot!")

def getStarted(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "mekina/getStarted.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "mekina/detail.html", {"question": question})

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, "mekina/detail.html", {"question": question})
    #return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of queston %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)