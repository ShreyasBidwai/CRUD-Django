from django.shortcuts import render
from django.http import HttpResponse


def recipe(requests):
    return render(requests, 'recipe.html')
