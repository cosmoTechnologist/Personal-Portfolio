from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

def index (request):
	return render(request, 'website/index.html', {})


