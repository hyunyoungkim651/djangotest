# from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def index(request):
    # return HttpResponse("Hello, world. You're at the blog2 index.")
    # name = "khy"
    # return render(request, "index.html", { "name" : name })
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title= "hello",
    #     contents = "this is test",
    #     view_count = 0
    # )
    ctx = {
        "article_list" : article_list
    }

    return render(request, "index.html", ctx)
