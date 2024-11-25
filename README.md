# Django-проект сайта-визитки для дизайнера
<img src="https://github.com/Ninja2EatYa/diploma_dj_site/blob/main/colored3.jpg" align=left>

## О проекте

Этот проект представляет собой веб-приложение на Django, предназначенное для создания и управления портфолио своих проектов в сфере дизайна и не только. 
Он включает в себя различные страницы, такие как главная страница, страница "Обо мне", список проектов, страница конкретного проекта и страница контактов.
Пользователи могут просматривать информацию о проектах и отправлять запросы на установление контакта с владельцем сайта через форму обратной связи.

## Основные функции

- **Главная страница:** Отображает меню с возможностью попадания на другие страницы сайта.
- **Страница "Обо мне":** Предоставляет информацию о владельце портфолио проектов.
- **Список проектов:** Показывает все проекты, доступные в портфолио.
- **Страница проекта:** Детальное описание конкретного проекта с возможностью просмотра изображений с разработанным под проект дизайном.
- **Страница контактов:** Форма для отправки контактной информации владельцу сайта.

## Установка и запуск

### Требования

- Python 3.x
- Django 3.x
- PostgreSQL

### Установка PostgreSQL
1. Для Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install postgresql postgresql-contrib
   ```
2. Для macOS (с использованием Homebrew):
   ```bash
   brew install postgresql
   brew services start postgresql
   ```
3. Для Windows:
   - Скачайте и установите PostgreSQL с [официального сайта](https://www.postgresql.org/download/windows/).

### Создание базы данных и пользователя:
1. Войдите в PostgreSQL:
   ```bash
   sudo -u postgres psql
   ```
2. Создайте базу данных:
   ```sql
   CREATE DATABASE dj_site_db;
   ```
3. Создайте пользователя и установите пароль:
   ```sql
   CREATE USER dj_site_user WITH PASSWORD 'your_password';
   ```
4. Предоставьте пользователю права на базу данных:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE dj_site_db TO dj_site_user;
   ```
5. Выйдите из psql:
   ```sql
   \q
   ```

### Настройка Django для использования PostgreSQL
1. Установите psycopg2:
   ```bash
   pip install psycopg2
   ```
2. Обновите настройки Django:
   - Откройте файл settings.py в директории dj_site_project/dj_site_project/.
   - Найдите раздел DATABASES и измените его на следующий:
   ```python
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dj_site_db',
         'USER': 'dj_site_user',
         'PASSWORD': 'your_password',
         'HOST': 'localhost',
         'PORT': '5432',
      }
   }
   ```

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Ninja2EatYa/diploma_dj_site
   cd diploma_dj_site
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate  # Для Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Примените миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Создайте суперпользователя (для доступа к админке):
   ```bash
   python manage.py createsuperuser
   ```
9. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
11. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/main/

## Структура проекта

   ```
   dj_site_project/
   ├── dj_site_app/
   │   ├── media/
   │   │   └── ...
   │   ├── migrations/
   │   │   ├── __init__.py
   │   │   └── ...
   │   ├── static/
   │   │   ├── backgrounds/
   │   │   │   └── ...
   │   │   ├── css/
   │   │   │   └── styles.css
   │   │   └── glightbox/
   │   │       ├── glightbox.min.css
   │   │       └── glightbox.min.js
   │   ├── templates/
   │   │   ├── about.html
   │   │   ├── contacts.html
   │   │   ├── main.html
   │   │   ├── project.html
   │   │   └── projects_list.html
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── tests.py
   │   ├── urls.py
   │   ├── views.py
   ├── dj_site_project/
   │   ├── __init__.py
   │   ├── asgi.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── .env
   ├── .gitignore
   ├── dj_site_project/
   ├── manage.py
   └── requirements.txt
   ```
### Можно использовать библиотеку decouple и метод config для сохранения персональных данных отдельно от файла settings.py в файле .env:
1. Для этого установите ее:
   ```bash
   pip install python-decouple
   ```
2. Затем необходимо создать файл .env в корневой директории проекта в котором прописать те данные, которые необходимо безопасно хранить локально на компьютере. Например:
   ```python
   USERNAME = 'username'
   PASSWORD = 'password'
   ```
3. Теперь необходимо импортировать метод config в settings.py и использовать следующий принцип записи:
   ```python
   "USER": config("USERNAME"),
   "PASSWORD": config("PASSWORD"),
   ```
### Приложение dj_site_app
- models.py: Определение моделей данных, включая Project, ProjectImage, About, и ReplyField.
- views.py: Определение функций представлений для обработки запросов и отображения соответствующих шаблонов.
- urls.py: Конфигурация URL-шаблонов для маршрутизации запросов к соответствующим представлениям.
- admin.py: Настройка административного интерфейса Django для управления моделями.
- apps.py: Конфигурация приложения.

### Шаблоны
- main.html: Главная страница.
- about.html: Страница "Обо мне".
- projects_list.html: Страница со списком проектов.
- project.html: Страница конкретного проекта.
- contacts.html: Страница контактов.

### Статические файлы
- styles.css: Основные стили для всего сайта.
- glightbox.min.css: Стили для карусели изображений.
- glightbox.min.js: Скрипт для карусели изображений.

В проекте использован репозиторий GlightBox, который расположен по адресу: https://github.com/biati-digital/glightbox/tree/master

## Использование

### Административная панель
1. Войдите в административную панель по адресу http://127.0.0.1:8000/admin/.
2. Добавьте и управляйте проектами, изображениями, информацией о себе и контактами через интерфейс администратора.

### Форма обратной связи
1. Перейдите на страницу контактов.
2. Заполните форму и отправьте ее владельцу сайта. Данные будут сохранены в базе данных.

## Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, сделайте форк репозитория и отправьте pull request с вашими изменениями.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по адресу 777jamesholden@gmail.com

# Спасибо за использование этого проекта!

[![Go to my GitHub page](https://img.shields.io/badge/Go_to_my_GitHub_page-grey?style=flat&logo=github&labelColor=yellow&color=grey&link=https%3A%2F%2Fgithub.com%2FNinja2EatYa%2F
)](https://github.com/Ninja2EatYa)
