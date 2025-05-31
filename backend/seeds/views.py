from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.http import QueryDict

from .models import Seed, Type
from .forms import Feedback, Search


def index(request):
    template = 'seeds/index.html'
    title = 'Семяна'
    context = {
        'title': title,
    }
    return render(request, template, context)


def seeds(request: HttpRequest):
    # print()
    # print(request)
    # print(request.scheme)
    # print(request.body)
    # print(request.path)
    # print(request.path_info)
    # print(request.method)
    # print(request.encoding)
    # print(request.content_type)
    # print(request.content_params)
    # print(request.GET)
    # print(request.POST)

    # print(request.COOKIES)
    # print(request.FILES)
    # print()
    # print(request.META)
    # print()
    # print(request.headers)
    # print(request.resolver_match)
    # print()
    if request.method == 'POST':
        template = 'seeds/submitted_form.html'
        title = 'Запрос отправлен'
        request.content_params
        context = {
            'title': title,
            'referer': request.META.get('HTTP_REFERER'),
        }
        return render(request, template, context)
    search_form = Search()
    feedback_form = Feedback()
    
    seed_list = Seed.objects.all()
    if request.GET.get('type'):
        type_obj = Type.objects.get(translit=request.GET.get('type'))
        seed_list = seed_list.filter(type=type_obj)
        search_form.fields['type'].initial = (request.GET.get('type'), type_obj.name)
    if request.GET.get('seed_pattern'):
        seed_list = seed_list.filter(name__icontains=request.GET.get('seed_pattern'))
        search_form.fields['seed_pattern'].initial = request.GET.get('seed_pattern')

    paginator = Paginator(seed_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'seeds/seeds.html'
    title = 'Каталог семян'
    context = {
        'title': title,
        'page_obj': page_obj,
        'search_form': search_form,
        'feedback_form': feedback_form,
    }
    return render(request, template, context)

def seed_name(request, type, name):
    seed = Seed.objects.get(type=Type.objects.get(translit=type),
                            translit=name)
    template = 'seeds/seed_profile.html'
    title = f'{type}: {name}'
    context = {
        'title': title,
        'type': type,
        'name': name,
        'referer': request.META.get('HTTP_REFERER'),
        'seed': seed,
    }
    return render(request, template, context)

def submitted_form(request):
    print(request.META.get('HTTP_REFERER'))
    template = 'seeds/submitted_form.html'
    title = 'Запрос отправлен'
    context = {
        'title': title,
        'referer': request.META.get('HTTP_REFERER'),
    }
    return render(request, template, context)
