from django.shortcuts import render
from .models import Article

def index(request):
    return render(request, 'main/index.html')

def schedule(request):
    return render(request, 'main/schedule.html')

def register(request):
    return render(request, 'main/register.html')

def article(request):
    article = Article.objects.all()
    return render(request, 'main/article.html', {'article': article})
