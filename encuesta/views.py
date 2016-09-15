from django.shortcuts import render

from .models import pregunta

def index(request):
	lastest_pregunta_list = pregunta.objects.order_by('-pub_fecha')[:5]
	context = {
		'lastest_pregunta_list': lastest_pregunta_list,
	}
	return render(request, 'encuesta/index.html', context)

	

def detail(request, pregunta_id):
    return HttpResponse("You're looking at question %s." % pregunta_id)

def results(request, pregunta_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % pregunta_id)

def vote(request, pregunta_id):
    return HttpResponse("You're voting on question %s." % pregunta_id)