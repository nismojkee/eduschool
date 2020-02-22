from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request):
	return render(
		request,
		'index.html',
		{
			'title':'Online IT school',
			'year': datetime.now().year,
		}
	)