from django.urls import path
from . import views

urlpatterns = [
	path('', views.indexView, name='home'),
	path('pwReset/', views.pwResetView, name='pwReset')
]