from django.views import View
from django.http import JsonResponse
import json
import requests


# Create your views here.
class ListaNoticias(View):
    def get(self, request, noticia=0):
        lista=[]
        print(noticia)
        if noticia == 0:
            url = 'https://www.ulagos.cl/wp-json/wp/v2/posts'
            
            pagina = requests.get(url)
            datos = json.loads(pagina.content)
            
            for i  in datos:
                dato = {"id": i['id'], 'titulo' : i['title'], 'resumen': i['excerpt']} 
                lista.append(dato)
        else: 
            url = 'https://www.ulagos.cl/wp-json/wp/v2/posts/'+ str(noticia)
            
            
            pagina = requests.get(url)
            datos = json.loads(pagina.content)
            dato= {'id': datos.get('id'), 'titulo': datos.get('title'), 'notica_completa': datos.get('content')}
            lista.append(dato)
            
        return JsonResponse(lista, safe=False)
    