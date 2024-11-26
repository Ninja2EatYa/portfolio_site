"""
Модуль конфигурации URL содержит URL-шаблоны,
которые сопоставляют различные URL-пути с
соответствующими функциями представлений.

Основные URL-шаблоны включают главную страницу,
страницу "Обо мне", список проектов, страницу
конкретного проекта и страницу контактов.
"""

from django.urls import path
from .views import main, about, projects_list, project, contacts


urlpatterns = [
    # Главная страница
    path('', main, name='main'),
    # Страница "Обо мне"
    path('about/', about, name='about'),
    # Страница со списком проектов
    path('projects_list/', projects_list, name='projects_list'),
    # Страница проекта с динамическим параметром, соответствующим id проекта
    path('projects_list/project/<int:project_id>/', project, name='project'),
    # Страница контактов
    path('contacts/', contacts, name='contacts'),
]
