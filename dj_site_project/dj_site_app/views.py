from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def main(request):
    context = {
        'page': 'Главная',
        'header': 'John Doe',
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
    projects_list = Project.objects.all().order_by('-id')
    context = {
        'page': 'Проекты',
        'header': 'Мои проекты:',
        'footer': 'Москва. 2024',
        'projects_list': projects_list,
    }
    return render(request, 'projects_list.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'page': project.title,
        'header': project.title,
        'footer': 'Москва. 2024',
        'project': project,
        'images': project.images.all(),
    }
    return render(request, 'project.html', context)


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
