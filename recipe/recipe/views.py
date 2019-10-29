from django.shortcuts import render
from recipe.models import Recipe, Author, Recipe



def index(request):
    html = "index.html"

    news = Recipe.objects.all()

    return render(request, html, {'data': news})

def author_view(request,id):
    html = "author.html"

    auth = Author.objects.filter(id=id)

    recipes = Recipe.objects.filter(author=auth.first())

    return render(request,html,{"auth":auth,"recipes":recipes})

def recipe_view(request,id):
    html = "recipe.html"

    reci = Recipe.objects.filter(id=id)

    return render(request,html,{"reci":reci})