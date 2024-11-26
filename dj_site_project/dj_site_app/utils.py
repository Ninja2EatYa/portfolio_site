"""
Модуль для утилит.
Содержит функцию для уменьшения размеров изображений,
сохраняя их пропорции, при помощи библиотеки Pillow.
"""

from PIL import Image


def resize_image(image_path, width) -> None:
    """
    Функция уменьшает размер изображения, сохраняя пропорции.
    """
    img = Image.open(image_path)
    img.thumbnail((width, width), Image.Resampling.LANCZOS)
    img.save(image_path)
