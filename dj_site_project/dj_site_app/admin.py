from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'image_tag', 'created_at')
#
#     def image_tag(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
#         return "Нет изображения"
#
#     image_tag.short_description = 'Изображение'


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Количество пустых форм по умолчанию
    fields = ('image', 'order')
    ordering = ('order',)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'created_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(About)
admin.site.register(ReplyField)
