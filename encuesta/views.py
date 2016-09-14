from django.http import HttpResponse


def index(request):
    return HttpResponse("hola esta es la encuesta")