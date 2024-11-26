"""
Настройки административного интерфейса Django
с классами и встроенными моделями для управления
в административном интерфейсе
"""

from django.contrib import admin
from .models import Project, ProjectImage, About, ReplyField
from django.utils.html import mark_safe


class ProjectImageInline(admin.TabularInline):
    """
    Класс встроенной административной модели
    для загрузки изображений проекта через админ-панель
    """
    model = ProjectImage
    extra = 0  # Количество пустых форм по умолчанию
    fields = ('image', 'order', 'img_preview')
    ordering = ('order',)
    readonly_fields = ('img_preview',)


class ProjectAdmin(admin.ModelAdmin):
    """
    Класс административной модели проекта,
    включающий класс для изображений проекта
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


# Регистрация модели Project c настройками ProjectAdmin
admin.site.register(Project, ProjectAdmin)
# Регистрация модели ProjectImage с настройками по-умолчанию
admin.site.register(ProjectImage)
# Регистрация модели About с настройками по-умолчанию
admin.site.register(About)
# Регистрация модели ReplyField с настройками по-умолчанию
admin.site.register(ReplyField)
