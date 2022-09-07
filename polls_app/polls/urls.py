
from django.urls import path
from . import views

urlpatterns = [
    #ex: polls
    path("", views.index, name="index"),
    #ex: polls/5/detail
    path("details/<int:question_id>/", views.details, name="detail"),
    #ex: polls/5/results
    path("results/<int:question_id>/", views.results, name="result"),
    #ex: polls/5/vote
    path("vote/<int:question_id>/", views.votes, name="")
]
