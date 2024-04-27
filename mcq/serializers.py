from rest_framework import serializers
from .models import Quiz, Question, Answer, Category, Note

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
  answers = AnswerSerializer(many=True, read_only=True)

  class Meta:
    model = Question
    fields = ['id', 'text', 'answers']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
      model = Quiz
      fields = ['id', 'title', 'description', 'questions']

class CategorySerializer(serializers.ModelSerializer):
  quiz = QuizSerializer(many=True, read_only=True)
  
  class Meta:
    model = Category
    fields = ['id', 'name', 'description', 'quiz']

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ['id', 'text']