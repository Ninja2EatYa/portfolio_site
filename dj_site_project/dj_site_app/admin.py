from django.contrib import admin
from .models import Project, Menu, ReplyField
from django.utils.html import format_html

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag', 'created_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "Нет изображения"

    image_tag.short_description = 'Изображение'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Menu)
admin.site.register(ReplyField)
