from django.shortcuts import render
from django.http import HttpResponse
from .models import Perfils
# Create your views here.

def home(request):
	return render(request,'home.html', {'perfis' : Perfils.objects.all()})

def perfis(request, perfil_id):
	
	perfil = Perfils.objects.get(id=perfil_id);
	

	return render(request,'perfis.html',{"perfil" : perfil})