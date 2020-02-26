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
		}
	)

def courses(request):
	return render(
		request,
		'courses.html',
		{
			'title':'Courses list',
			'style':'courses',
		}
	)

def teachers(request):
	return render(
		request,
		'teachers.html',
		{
			'title':'Teachers staff',
			'style':'teachers',
		}
	)