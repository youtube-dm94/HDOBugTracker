from django.urls import path
from . import views
from .views import TicketCreate

app_name = "ticket"
urlpatterns = [
	path('', views.indexView, name='home'),
	path("create/", TicketCreate.as_view(), name='create')
]