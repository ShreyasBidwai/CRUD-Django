from django.shortcuts import render, redirect
from django.http import HttpResponse
from veggie.models import *

def recipe(request):
    if request.method == "POST":
        data=request.POST
        namer = data.get('namer')
        desc = data.get('desc')
        img = request.FILES.get('img')
        
        Recipe.objects.create(
            img=img,
            namer=namer,
            desc=desc
        )
        return redirect('/')

        
    return render(request, 'recipe.html')
