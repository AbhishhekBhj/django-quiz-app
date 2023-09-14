from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.Home),
    path("api/quiz/", view=views.get_quiz, name="quiz"),
    path("quiz/", view=views.quiz, name="quizs"),
]
