"""
Модуль представлений.
Содержит функции представлений, которые обрабатывают
различные запросы и отображают соответствующие шаблоны.

Каждая функция отвечает за отображение своей страницы:
- главная страница (main)
- страница "Обо мне" (about)
- страница списка проектов (projects_list)
- страница конкретного проекта (project)
- страница контактов (contacts), с обработкой формы обратной связи
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import About, Blog, Project, ReplyField
import logging


logger = logging.getLogger(__name__)


def main(request):
    """Возвращает главную страницу с названием и заголовком"""
    logger.info('Запрос на главную страницу')
    context = {
        'page': 'Главная',
        'header': 'Алиса Александрова',
    }
    return render(request, 'main.html', context)


def about(request):
    """
    Возвращает страницу "Обо мне" с названием и заголовком.
    Получает информацию "Обо мне" из модели About и
    отображает на странице. Если информация отсутствует,
    выводит сообщение об отсутствии информации.
    """
    logger.info('Запрос на страницу "Обо мне"')
    about_info = About.objects.first()
    if not about_info:
        logger.warning('Информация "Обо мне" отсутствует')
        return render(request, 'about.html',
                      {'about_text': 'Информация "Обо мне" отсутствует.'})
    context = {
        'page': 'Обо мне',
        'header': 'Обо мне:',
        'about_text': about_info.about,
    }
    return render(request, 'about.html', context)


def blog_list(request):
    """
    Возвращает страницу со списком постов блога
    с обработкой через пагинатор
    """
    logger.info('Запрос на страницу блога')
    posts = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    if not posts:
        logger.warning('Постов пока нет')
    context = {
        'page': 'Мой блог',
        'header': 'Мой блог',
        'page_object': page_object,
    }
    return render(request, 'blog.html', context)


def projects_list(request):
    """
    Возвращает страницу перечня проектов с названием и заголовком.
    Получает все проекты из модели Project, сортирует их
    по убыванию id и отображает на странице.
    """
    logger.info('Запрос на страницу списка проектов')
    projects_list = Project.objects.all().order_by('-id')
    if not projects_list:
        logger.warning('Проекты пока не загружены')
    context = {
        'page': 'Проекты',
        'header': 'Мои проекты:',
        'projects_list': projects_list,
    }
    return render(request, 'projects_list.html', context)


def project(request, project_id):
    """
    Возвращает страницу проекта с названием и заголовком.
    Получает проект по его id, если проект не найден,
    возвращает 404 ошибку.
    Отображает страницу проекта с его описанием и изображениями.
    """
    logger.info(f'Запрос на страницу проекта с id={project_id}')
    project = get_object_or_404(Project, id=project_id)
    context = {
        'page': project.title,
        'header': project.title,
        'project': project,
        'images': project.images.all(),
    }
    return render(request, 'project.html', context)


def contacts(request):
    """
    Возвращает страницу контактов с названием и заголовком.
    Обрабатывает POST-запрос для сохранения данных формы
    обратной связи. После обработки формы перенаправляет
    на главную страницу.
    """
    logger.info('Запрос на страницу контактов')
    context = {
        'page': 'Контакты',
        'header': 'Свяжитесь со мной:',
    }
    if request.method == "POST":
        try:
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
            logger.info(
                f'Форма обратной связи получена от: {first_name} {second_name}'
            )
            return redirect('main')
        except Exception as err:
            logger.error(f'Ошибка при обработке формы обратной связи: {err}')
    return render(request, 'contacts.html', context)
