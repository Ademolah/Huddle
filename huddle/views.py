from django.shortcuts import render
from .models import Huddle

# Create your views here.

def index(request):

    return render(request, 'huddle/index.html', )

def huddle(request):

    key = request.GET.get('key','')
    user = request.GET.get('user', '')
    huddle, created = Huddle.objects.get_or_create(key=key)

    return render(request, 'huddle/huddle.html', {
        'user': user
    })
