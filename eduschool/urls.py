from django.contrib import admin
from django.urls import path
from content import views

urlpatterns = [
	path('', views.index, name='index'),
	path('courses', views.courses, name='courses'),
	path('teachers', views.teachers, name='teachers'),
    path('admin/', admin.site.urls),
]
