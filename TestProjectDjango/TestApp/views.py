from django.shortcuts import render


def index(request):
    return render(request, 'TestApp/index.html', {"title": "Head from index"})


def about(request):
    return render(request, 'TestApp/about.html')


def content(request):
    return render(request, 'TestApp/content.html')
