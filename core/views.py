from django.shortcuts import render
from main.models import Main

def home(request):
    main = Main.objects.last()

    return {
        'main': main,
    }



def handler500(request):
    return render(request, '500.html', status=500)
