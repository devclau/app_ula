from django.core.serializers import serialize
from django.shortcuts import render
from django.views import View
from pre_frecuentes.models import Pregunta
from django.http import JsonResponse, HttpResponse

# Create your views here.
class ListaFrecuentes(View):
    def get(self, request, *args, **kwargs):
        p=[]
        preguntas = Pregunta.objects.all()
        
        for i in preguntas:
            categoria_dict = i.categoria.to_dict()
            p.append({'id':i.id, 'titulo': i.titulo, 'respuesta':i.respuesta, 'categoria':categoria_dict} )
        return JsonResponse(p, safe=False)
        