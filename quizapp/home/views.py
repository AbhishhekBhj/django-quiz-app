from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import random
from .models import Question, Category

# Create your views here.


def Home(request):
    context = {"categories": Category.objects.all()}

    if request.GET.get("category"):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request, "home.html", context=context)


def quiz(request):
    context = {"category": request.GET.get("category")}
    return render(request, "quiz.html", context=context)


def get_quiz(request):
    try:
        questions = Question.objects.all()

        if request.GET.get("category"):
            questions = questions.filter(
                # filter questioon by category
                category__name__icontains=request.GET.get("category")
            )
            questions = list(questions)
        data = []
        random.shuffle(questions)
        for question in questions:
            data.append(
                {
                    "uid": question.uid,
                    "question": question.question,
                    "marks": question.marks,
                    "category": question.category.name,
                    "answers": question.get_answer(),
                }
            )
        payload = {"status": True, "data": data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse("Unexpected Error")
