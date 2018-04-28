from django.shortcuts import render
from menu.models import Menu

# Create your views here.


def index(request, qs=Menu.objects.filter(is_main=True)):
    return render(request, template_name='index.html', context={'qs': qs})


def draw(request, slug):
    if Menu.objects.filter(slug=slug).first():
        return render(
            request, template_name='draw.html', context={'menu': slug})
    return index(request, qs=None)
