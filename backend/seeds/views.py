from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Seed, Type
from .forms import Feedback, Search


def index(request):
    template = 'seeds/index.html'
    title = 'Семяна'
    context = {
        'title': title,
    }
    return render(request, template, context)

def seeds(request):
    # if request.POST:
    #     return redirect('seeds', )
    search_form = Search()
    feedback_form = Feedback()

    seed_list = Seed.objects.all()
    if request.GET.get('type'):
        type = Type.objects.get(translit=request.GET.get('type'))
        seed_list = seed_list.filter(type=type)
        search_form.fields['type'].initial = (request.GET.get('type'), type.name)
    if request.GET.get('seed_pattern'):
        seed_list = seed_list.filter(name__icontains=request.GET.get('seed_pattern'))
        search_form.fields['seed_pattern'].initial = request.GET.get('seed_pattern')

    for field in search_form:
        print(field)

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

