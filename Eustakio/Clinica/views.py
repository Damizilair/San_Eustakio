from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def especialidades(request):
    return HttpResponse("Vista especialidades")

def doctores(request):
    return HttpResponse("Vista doctores")

def pacientes(request):
    return HttpResponse("Vista pacientes")

def medicamentos(request):
    return HttpResponse("Vista medicamentos")


