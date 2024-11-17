from django.shortcuts import render, redirect
from .models import *


def main(request):
    context = {
        'page': 'Главная',
        'header': 'Александрова Алиса',
        'footer': 'Москва. 2024',
    }
    return render(request, 'main.html', context)


def about(request):
    about_info = About.objects.first()  # Предполагается, что существует только одна запись
    if about_info is None:
        return render(request, 'about.html', {'about_text': 'Информация отсутствует.'})
    context = {
        'page': 'Обо мне',
        'header': 'Обо мне:',
        'footer': 'Москва. 2024',
        'about_text': about_info.about,
        'about_contacts': about_info.contacts,
    }
    return render(request, 'about.html', context)


def projects_list(request):
    projects_list = Project.objects.all()
    context = {
        'page': 'Проекты',
        'header': 'Мои проекты:',
        'footer': 'Москва. 2024',
        'projects': projects_list,
    }
    return render(request, 'projects.html', context)


def contacts(request):
    context = {
        'page': 'Контакты',
        'header': 'Свяжитесь со мной:',
        'footer': 'Москва. 2024',
    }
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
    return render(request, 'contacts.html', context)
