from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list,
    })


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, "polls/details.html", {
        "question": question,
    })


def results(request, question_id):
    return HttpResponse(f"This is the Results of the question number: {question_id}")


def votes(request, question_id):
    return HttpResponse(f"You arte voting for question number: {question_id}")
