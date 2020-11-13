from django.shortcuts import render
from django.core.paginator import Paginator

def paginate(request, object_list, per_page=5):
    paginator= Paginator(object_list, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return page

questions = [
    {
        'id': idx,
        'title': f'{idx}. How to build a moon park?',
        'text': f'Guys, i have trouble with a moon park. Can\'t find the black-jack... It\'s text number {idx}!',
    } for idx in range(50)
]

def index(request):
    page = paginate(request, questions)
    return render(request, 'index.html', {
        'questions': page,
    })

def hot(request):
	return render(request, 'hot.html', {
        'questions': questions,
    })

def add_question(request):
	return render(request, 'add_question.html', {})

def registration(request):
	return render(request, 'registration.html', {})

def log_in(request):
	return render(request, 'log_in.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def question_by_tag(request, string):
	return render(request, 'question_by_tag.html', {
        'questions': questions,
        'string':string,
	})

def answer(request, pk):
	question = questions[pk]
	return render(request, 'answer.html', {
        'question': question,
	})
