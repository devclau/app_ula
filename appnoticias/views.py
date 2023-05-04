from django.views import View
from django.http import JsonResponse
import json
import requests
from bs4 import BeautifulSoup


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
                dato = {"id": i['id'], 'titulo' : i['title'], 'resumen': i['excerpt'], 'categories': i['categories']} 
                lista.append(dato)
        else: 
            url = 'https://www.ulagos.cl/wp-json/wp/v2/posts/'+ str(noticia)
            
            
            pagina = requests.get(url)
            datos = json.loads(pagina.content)
            dato= {'id': datos.get('id'), 'titulo': datos.get('title'), 'noticia_completa': datos.get('content')}
            lista.append(dato)
            
        return JsonResponse(lista, safe=False)

    def scrapring(request):
        url = 'https://www.ulagos.cl/'
        urlopen  = requests.get(url)
        soup = BeautifulSoup(urlopen.content, "html.parser" )

        html_contenido = soup.find_all("div", {"class":"ultimas-noticias"})
        lista_contenido = []

        for contenido in html_contenido:
            imagen =  contenido.find('img').get('src')
            titulo = contenido.find('span', {'class':'titulo-ultima-noticia'}).text
            categoria = contenido.find('span', {'class':'color-categoria'}).text
            link = contenido.find('a').get('href')
            lista_contenido.append([{
                'imagen': imagen,
                'titulo':titulo,
                'categoria':categoria,
                'link' : link 
                }],)
            
        return JsonResponse(lista_contenido, safe=False)
    