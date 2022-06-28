from multiprocessing import context
from django.shortcuts import render

from .models import Carusel

from django.template import loader
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	carusel = Carusel.objects.all()

	context = {
		'carusel': carusel
	}

	return render(request, 'template/home.html', context)
