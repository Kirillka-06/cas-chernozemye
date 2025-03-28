from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Seed, Type


def index(request):
    template = 'seeds/index.html'
    title = 'Семяна'
    context = {
        'title': title,
    }
    return render(request, template, context)

def seeds(request):
    type_list = Type.objects.all()
    seed_list = Seed.objects.all()
    paginator = Paginator(seed_list, 8) 

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    template = 'seeds/seeds.html'
    title = 'Каталог семян'
    context = {
        'title': title,
        'type_list': type_list,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def seed_name(request, type, name):
    seed = Seed.objects.get(type=Type.objects.get(translit=type),
                            translit=name)
    template = 'seeds/seed_name.html'
    title = f'{type}: {name}'
    context = {
        'title': title,
        'type': type,
        'name': name,
        'referer': request.META.get('HTTP_REFERER'),
        'seed': seed,
    }
    return render(request, template, context)

