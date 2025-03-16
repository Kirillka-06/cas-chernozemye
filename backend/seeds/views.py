from django.shortcuts import render


def index(request):
    template = 'seeds/index.html'
    title = 'Семяна'
    context = {
        'title': title,
    }
    return render(request, template, context)

def seed_variety(request, type, variety):
    template = 'seeds/seed_variety.html'
    title = f'{type} {variety}'
    context = {
        'title': title,
        'type': type,
        'variety': variety,
    }
    return render(request, template, context)
    #return HttpResponse(f'Семяна {type} {variety}')

