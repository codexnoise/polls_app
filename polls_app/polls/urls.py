
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    #ex: polls
    path("", views.IndexView.as_view(), name="index"),
    #ex: polls/5/detail
    path("details/<int:pk>/",
         views.DetailsView.as_view(), name="details"),
    #ex: polls/5/results
    path("results/<int:pk>/",
         views.ResultsView.as_view(), name="results"),
    #ex: polls/5/vote
    path("vote/<int:question_id>/", views.votes, name="votes")
]
