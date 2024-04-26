import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizu.settings')
application = get_wsgi_application()



from mcq.models import Category, Quiz, Question, Answer
from outDBTask.question import Questions

quizId = 2
quiz = Quiz.objects.get(id=quizId)

def showOutput():
  print('\n \n ***the questions counts is*** ', Question.objects.count())
  print('\n \n ***the answers counts is *** ' , Answer.objects.count())

def removePrev():
  with open(os.path.join('outDBTask', 'latestQuestionId.txt'), 'r', encoding='utf-8') as file:
    data = file.read()
    with open(os.path.join('outDBTask', 'backUpQuestionId.txt'), 'a', encoding='utf-8') as file2:
      file2.write(data)
  with open(os.path.join('outDBTask', 'latestQuestionId.txt'), 'w', encoding='utf-8'):
    pass

  with open(os.path.join('outDBTask', 'latestQuestion.txt'), 'r', encoding='utf-8') as file3:
    data2 = file3.read()
  with open(os.path.join('outDBTask', 'backupQuestion.txt'), 'a', encoding='utf-8') as file4:
    file4.write(data2)
  with open(os.path.join('outDBTask', 'latestQuestion.txt'), 'w',  encoding='utf-8'):
    pass

def createPrev(question, answers):
  with open(os.path.join('outDBTask', 'latestQuestionId.txt'), 'a', encoding='utf-8') as f:
    f.write(str(question.id ) + " ")
  with open(os.path.join('outDBTask', 'latestQuestion.txt'), 'a', encoding='utf-8') as f:
    f.write(f'Question ID: {question.id}\n')
    print('the question.txt is***', question.text)
    f.write(f'Question: {question.text}\n')
    f.write('Answers:\n')
    for answer in answers:
      f.write(f'  - {answer[0]} (Correct: {answer[1]})\n')
    f.write('\n \n \n')

def validated_answers(answers):
    if len(answers) != 4:
        return False
    if not any(answer[1] for answer in answers):
        return False
    return True

def delete_latest_questions():
  with open(os.path.join('outDBTask', 'latestQuestionId.txt'), 'r', encoding='utf-8') as file:
    data = file.read().strip()
    data = data.replace('\n', ' ')
    data = data.split(" ")
    for id in data:
      id = int(id)
      question = Question.objects.get(id=id)
      question.delete()
      print('Question deleted...')

def createAnswers(question, answers):
  if validated_answers(answers):
    print("** The answers are valid **")
    for answer in answers:
      newAnswer = Answer.objects.create(text=answer[0], question=question, is_correct=answer[1])
      newAnswer.save() 
      print("The answer is created...")
    createPrev(question, answers)
  else:
    print("** The answers are not valid **")
    question.delete()
    
def createQuestions (quiz, questions):
  removePrev()
  for question in questions:
    questionVar = Question.objects.create(text=question['question'], quiz=quiz)
    questionVar.save()
    questionObj = Question.objects.get(id=questionVar.id)
    createAnswers(questionObj, question['answers'])
  


createQuestions(quiz, Questions)
# delete_latest_questions()










showOutput()
