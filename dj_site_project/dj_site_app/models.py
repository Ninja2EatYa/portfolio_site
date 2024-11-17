from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    about = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.about


class ReplyField(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=False)
    request_box = models.TextField(null=False, max_length=500, help_text='Максимальное количество: 500 символов')
    email = models.EmailField(null=False, help_text='Укажите адрес своего e-mail')
    phone = models.CharField(null=False, max_length=50, help_text='Укажите номер телефона для связи')

    def __str__(self):
        return self.first_name
