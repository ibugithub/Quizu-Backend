from django.contrib import admin
from .models import Quiz, Question, Answer, Category

registerModel = [ Quiz, Question, Answer, Category]
admin.site.register(registerModel)