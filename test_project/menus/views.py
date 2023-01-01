from django.shortcuts import render
from django.http import HttpResponse

def main(request, pk=None):
    return render(request, 'menus/home.html' , {"pk" : pk})
