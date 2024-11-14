from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# def get_page(request, page):
#     return HttpResponse(f'{page}')


def main(request):
    context = {
        'page': 'Добро пожаловать!',
        'header': 'Александрова Алиса',
        'current_year': 2024,
    }
    return render(request, 'main.html', context)


def about(request):
    menu_info = Menu.objects.first()  # Предполагается, что существует только одна запись
    context = {
        'about_text': menu_info.about,
        'background_image': menu_info.background_image,
    }
    return render(request, 'about.html', context)


def projects(request):
    projects_list = Project.objects.all()
    context = {
        'projects': projects_list,
    }
    return render(request, 'projects.html', context)


def contacts(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        request_box = request.POST.get('request_box')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reply = ReplyField(
            first_name=first_name,
            second_name=second_name,
            request_box=request_box,
            email=email,
            phone=phone
        )
        reply.save()
        return redirect('main')
    return render(request, 'contacts.html')
