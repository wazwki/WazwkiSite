''' Configurate functions and classes for rendering html pages '''

from django.shortcuts import render

from .git_contributions_package import contribution_color


def index(request):
    '''main page'''
    hello = "Добро пожаловать на главную страницу!"
    info = "Здесь будет ваш контент..."
    title = "Главная Страница"
    data = {"hello": hello, "info": info, "title": title}
    return render(request, "index.html", context=data)

def contact(request):
    '''contact page'''    
    hello = "Добро пожаловать на контактную страницу!"
    info = "Здесь будет ваш контент..."
    title = "Контакты"
    data = {"hello": hello, "info": info, "title": title}
    return render(request, "index.html", context=data)

def resume(request):
    '''resume page'''
    hello = "Добро пожаловать на страницу с резюме!"
    info = "Здесь будет ваш контент..."
    title = "Резюме"
    data = {"hello": hello, "info": info, "title": title}
    return render(request, "index.html", context=data)

def about(request):
    '''about site page'''
    hello = "Добро пожаловать на страницу обо мне!"
    info = "Здесь будет ваш контент..."
    title = "Обо мне"
    year = contribution_color()
    data = {"hello": hello, "info": info, "title": title, "year":year}
    return render(request, "gitc.html", context=data)

def page_not_found(request, exception):
    '''for 404 error page'''
    hello = "404"
    info = "Page not found"
    title = "404"
    data = {"hello": hello, "info": info, "title": title}
    return render(request, "notfound.html", context=data)
