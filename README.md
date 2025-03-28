# cas-chernozemye
An official site of CAS Chernozemye company

# Скачивание репозитория локально
- Скачайте проект: `git clone git@github.com:Kirillka-06/cas-chernozemye.git`

# Перед запуском проекта
- Перейдите в папку `backend/`
- Создайте файл виртуального окружения `.env` по образцу `.env.example`
- Создайте виртуальное окружение: `python -m venv venv`
- Активируйте виртуальное окружение: `source venv/Scripts/activate`
- Скачайте все зависимости: `pip install -r requirements.txt`

### Создание SECRET_KEY
- Запустите django-admin shell: `python manage.py shell`
- Напишите две строчки: `from django.core.management.utils import get_random_secret_key` и `get_random_secret_key()`
- Скопируйте полученный ключ и вставьте его в поле `SECRET_KEY` после `=` в файле `.env`

# Запуск проекта локально
- Напишите в консоли `python manage.py migrate`
- Запустите локальный сервер: `python manage.py runserver`

### Создание суперюзера
- Напишите в консоли `python manage.py createsuperuser`
- Перейдите на сайт `http(s)://<hostname>/admin/`
> Для локального сервера: `http://127.0.0.1:8000/admin/`

