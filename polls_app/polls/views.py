from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>polls app index</h1>")


def details(request, question_id):
    return HttpResponse(f"This is the question number: {question_id}")


def results(request, question_id):
    return HttpResponse(f"This is the Results of the question number: {question_id}")


def votes(request, question_id):
    return HttpResponse(f"You arte voting for question number: {question_id}")
