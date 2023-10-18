from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('content', views.content, name='content'),
    path('news/<int:news_id>', views.detail_news, name='news_detail')
]
