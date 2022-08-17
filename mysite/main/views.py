from multiprocessing import context
from django.shortcuts import render

from .models import Carusel

from django.template import loader
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	carusels = Carusel.objects.all()

	context = {
		'carusels': carusels
	}
	for carusel in carusels:
		print(carusel.title)

	return render(request, 'pages/home.html', context)
