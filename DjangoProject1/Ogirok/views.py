from django.shortcuts import render

def home(request):
    context = {'title': 'Головна сторінка'}
    return render(request, 'ogirok/home.html', context)

def page1(request):
    return render(request, 'Ogirok/page.html', {'title': 'Сторінка 1'})

def page2(request):
    return render(request, 'Ogirok/page.html', {'title': 'Сторінка 2'})

def page3(request):
    return render(request, 'Ogirok/page.html', {'title': 'Сторінка 3'})

def page4(request):
    return render(request, 'Ogirok/page.html', {'title': 'Сторінка 4'})

def page5(request):
    return render(request, 'Ogirok/page.html', {'title': 'Сторінка 5'})
from django.shortcuts import render
from .models import Tool

def tools_page(request):
    tools = Tool.objects.all()
    return render(request, 'Ogirok/tools_page.html', {'tools': tools})