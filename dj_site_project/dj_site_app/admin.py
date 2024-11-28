"""
Настройки административного интерфейса Django
с классами и встроенными моделями для управления
в административном интерфейсе
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import About, Project, ProjectImage, ReplyField
from django.utils.html import mark_safe


class ProjectImageInline(admin.TabularInline):
    """
    Встроенная модель для загрузки изображений
    проекта через админ-панель
    """
    model = ProjectImage
    extra = 0  # Количество пустых форм по умолчанию
    fields = ('image', 'order', 'img_preview')
    ordering = ('order',)
    readonly_fields = ('img_preview',)


class ProjectAdmin(admin.ModelAdmin):
    """
    Кастомизация административной панели
    для модели проекта, включающая встроенную
    модель для загрузки изображений
    """
    inlines = [ProjectImageInline]
    list_display = ('title', 'created_at', 'img_preview')

    def img_preview(self, obj) -> str:
        """
        Генерация HTML с предварительным просмотром
        изображений проекта в списке проектов в админ-панели
        """
        images = obj.images.all()
        if images:
            return mark_safe(''.join([
                f'<img src="{img.image.url}"'
                f'style="max-width: 100px; max-height: 100px;'
                f'margin-right: 5px;" />'
                for img in images
            ]))
        return "Нет изображения"

    img_preview.short_description = 'Изображение'


class MyAdminSite(admin.AdminSite):
    """
    Кастомизация административной панели
    с настройкой наименований полей
    """
    site_header = "Управление сайтом"
    site_title = "Админ-панель"
    index_title = "Разделы"


admin_site = MyAdminSite()

# Регистрация встроенной модели User с настройками UserAdmin.
admin_site.register(User, UserAdmin)
# Регистрация модели About с настройками по-умолчанию
admin_site.register(About)
# Регистрация модели Project c настройками ProjectAdmin
admin_site.register(Project, ProjectAdmin)
# Регистрация модели ReplyField с настройками по-умолчанию
admin_site.register(ReplyField)
# Регистрация модели ProjectImage с настройками по-умолчанию
admin_site.register(ProjectImage)
