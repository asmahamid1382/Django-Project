from django.shortcuts import render
from .models import lesson,quize

def get_word(request):
    context = {'words':lesson.objects.all()}
    return render(request,'get_word.html',context)

def add_word(request):
    if request.method == "GET":
        return render(request,'form.html')
    elif request.method == "POST":
        data = request.POST
        lesson.objects.create(word=data['word'],comonmistake_1=data['comonmistake_1'],comonmistake_2=data['comonmistake_2'],comonmistake_3=data['comonmistake_3'])
        return render(request,'finish.html')


def result(request):
    if request.method == 'POST':
        print(request.POST)
        questions=quize.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
        }
        return render(request,'result.html',context)
    else:
        questions=quize.objects.all()
        context = {'questions':quize.objects.all()} 
        return render (request,'quizes.html',context)