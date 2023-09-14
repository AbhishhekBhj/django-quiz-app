from django.db import models
import uuid
import random

# Create your models here.


# base class
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True  # this will be the base class


# class for category of questions
class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class for questions
class Question(BaseModel):
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answer(self):
        # Use the related_name 'question_ans' to get related Answer objects
        answer_objects = list(self.question_ans.all())
        random.shuffle(answer_objects)
        data = []
        for answer_object in answer_objects:
            data.append(
                {"answer": answer_object.answer, "is_correct": answer_object.is_correct}
            )
        return data


# class for answers
class Answer(BaseModel):
    question = models.ForeignKey(
        Question, related_name="question_ans", on_delete=models.CASCADE
    )
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.answer}"
