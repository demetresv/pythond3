from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import  ArticleForm


def home(request):
    articleform = ArticleForm()

    if request.method == 'GET':
        articlefrom = ArticleForm(request.GET)
        if articlefrom.is_valid():
            articlefrom.save()

    posts = Article.objects.all()
    context = {'articles': articles,
               'form': postfrom}

    return render(request, 'article.html', context=context)


def create_article(request):
    if request.method == 'POST':
        articleform = ArticleForm(request.POST)
        if articleform.is_valid():
            articleform.save()
    return render(request, 'create_article.html.html', context={'form': ArticleForm()})