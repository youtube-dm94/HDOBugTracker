import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def indexView(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

from django.views.generic.edit import CreateView
from .models import Ticket

class TicketCreate(CreateView):
	model = Ticket
	fields = ['description']
	template_name_suffix = '_create'
	success_url = '/'