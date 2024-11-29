"""
Модели данных для приложения Django, которые
представляют таблицы базы данных и их отношения.

Представлены три основные модели для разделов "Обо мне",
"Мои проекты" и "Контакты", а также модель для загрузки
изображений в раздел "Мои проекты"
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import resize_image


class About(models.Model):
    """Модель раздела "Обо мне" с текстовым полем"""
    about = models.TextField(verbose_name='Содержание раздела')

    class Meta:
        verbose_name = 'ОБО МНЕ'
        verbose_name_plural = 'ОБО МНЕ'

    def __str__(self) -> str:
        return self.about


class Blog(models.Model):
    """Модель для блог-постов"""
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок блога'
    )
    content = models.TextField(
        verbose_name='Содержание блога'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время изменения'
    )
    image = models.ImageField(
        upload_to='media/blog/image/',
        null=True,
        blank=True,
        verbose_name='Файл изображения'
    )
    video = models.FileField(
        upload_to='media/blog/video/',
        null=True,
        blank=True,
        verbose_name='Файл видео'
    )

    class Meta:
        verbose_name = 'МОЙ БЛОГ'
        verbose_name_plural = 'МОЙ БЛОГ'

    def __str__(self) -> str:
        return self.title


@receiver(post_save, sender=Blog)
def resize_blog_image_on_save(sender, instance, **kwargs) -> None:
    """
    Сигнал для автоматического уменьшения размеров изображения
    при сохранении экземпляра модели BlogPost.
    """
    if instance.image:
        resize_image(instance.image.path, 1920)


class Project(models.Model):
    """
    Модель раздела "Мои проекты" с названием проекта,
    его описанием и датой создания.
    """
    title = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        verbose_name='Наименование проекта'
    )
    description = models.TextField(
        null=True,
        verbose_name='Описание проекта'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'ПРОЕКТ'
        verbose_name_plural = 'ПРОЕКТЫ'

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
        Project,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='media/project/',
        null=True,
        verbose_name='Файл изображения'
    )
    order = models.PositiveIntegerField(
        default=2,
        verbose_name='Порядок отображения на сайте'
    )

    class Meta:
        verbose_name = 'Изображение и проект'
        verbose_name_plural = 'Все изображения'
        ordering = ['order']

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


@receiver(post_save, sender=ProjectImage)
def resize_project_image_on_save(sender, instance, **kwargs) -> None:
    """
    Сигнал для автоматического уменьшения размеров изображения
    при сохранении экземпляра модели ProjectImage.
    """
    if instance.image:
        resize_image(instance.image.path, 1920)


class ReplyField(models.Model):
    """
    Модель раздела "Контакты" с полями для
    ручного ввода посетителем сайта
    """
    first_name = models.CharField(
        max_length=30,
        null=False,
        verbose_name='Имя'
    )
    second_name = models.CharField(
        max_length=30,
        null=False,
        verbose_name='Фамилия'
    )
    request_box = models.TextField(
        null=False,
        max_length=500,
        verbose_name='Сообщение'
    )
    email = models.EmailField(
        null=False,
        verbose_name='E-mail'
    )
    phone = models.CharField(
        null=False,
        max_length=50,
        verbose_name='Телефон'
    )

    class Meta:
        verbose_name = 'КОНТАКТ'
        verbose_name_plural = 'КОНТАКТЫ'

    def __str__(self) -> str:
        return self.first_name
