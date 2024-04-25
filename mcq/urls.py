from django.urls import path 
from . import views

urlpatterns = [
  path('show_category/', views.CategoryViewSet.as_view({'get': 'list'}), name='show_category'),
  path('show_quiz/', views.QuizViewSet.as_view({'get': 'list'}), name='show_quiz'),
  path('show_questions/', views.QuestionViewSet.as_view({'get': 'list'}), name='show_questions'),
  path('show_answers/', views.AnswerViewSet.as_view({'get': 'list'}), name='show_answers'),
]