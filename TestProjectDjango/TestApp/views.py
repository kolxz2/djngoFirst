from django.shortcuts import render, get_object_or_404

from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'TestApp/index.html', {'news': news})


def about(request):
    return render(request, 'TestApp/about.html')


def detail_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'TestApp/detail_news.html', {'detail_news': news})


def content(request):
    return render(request, 'TestApp/content.html')
