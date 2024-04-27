from django.contrib import admin
from .models import Quiz, Question, Answer, Category, Tag, Note


from django.contrib import admin
from .models import Quiz, Question, Answer, Category

class QuizAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Quiz._meta.fields]

class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

class NoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)