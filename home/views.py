from django.shortcuts import render
from django.http import HttpResponse


def home(requests):

    voters = [
        {'name' : 'Shreyas', 'age':22},
        {'name' : 'Ganesh', 'age':13},
        {'name' : 'Atharva', 'age':10},
        {'name' : 'Yash', 'age':14},
        {'name' : 'Bhagyesh', 'age':16},
    ]

    for voter in voters:
        print(voter)

    return render(requests, 'index.html', context={'voters':voters})