"""
Модели данных для приложения Django, которые
представляют таблицы базы данных и их отношения.

Представлены три основные модели для разделов "Обо мне",
"Мои проекты" и "Контакты", а также модель для загрузки
изображений в раздел "Мои проекты"
"""

from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import resize_image


class Project(models.Model):
    """
    Модель раздела "Мои проекты" с названием проекта,
    его описанием и датой создания.
    """
    title = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    """
    Модель для изображений раздела "Мои проекты"
    с указанием/привязкой проекта, самого изображения
    и порядка загруженных изображений (порядок нужен
    для определения изображения для превью).
    """
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='media/', null=True)
    order = models.PositiveIntegerField(default=2)

    def __str__(self) -> str:
        return f'Image for {self.project.title}'

    def img_preview(self) -> str:
        """
        Генерация HTML с предварительным просмотром
        изображений проекта в настройках проекта в админ-панели
        """
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}"'
                f'style="max-width: 100px; max-height: 100px;"/>'
            )
        return 'Нет изображения'

    img_preview.short_description = 'Изображение'

    class Meta:
        ordering = ['order']


@receiver(post_save, sender=ProjectImage)
def resize_image_on_save(sender, instance, **kwargs) -> None:
    """
    Сигнал для автоматического уменьшения размеров изображения
    при сохранении экземпляра модели ProjectImage.
    """
    if instance.image:
        resize_image(instance.image.path, 1920)


class About(models.Model):
    """Модель раздела "Обо мне" с текстовым полем"""
    about = models.TextField()

    def __str__(self) -> str:
        return self.about


class ReplyField(models.Model):
    """
    Модель раздела "Контакты" с полями для
    ручного ввода посетителем сайта
    """
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=False)
    request_box = models.TextField(null=False, max_length=500)
    email = models.EmailField(null=False)
    phone = models.CharField(null=False, max_length=50)

    def __str__(self) -> str:
        return self.first_name
