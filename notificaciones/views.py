from django.shortcuts import render
from django.views import View
from notificaciones.models import Notificacion
from django.http import JsonResponse
from datetime import datetime

class ListaNotificacion(View):
    def get(self, request, *args, **kwargs):
        mes_actual = datetime.now().month
        p=[]
        notificacion = Notificacion.objects.all().order_by('-date')[:15]
        #notificacion = Notificacion.objects.filter(date__month=mes_actual).order_by('-date')
        for i in notificacion:
            p.append({'date':i.date, 'time': i.time, 'link':i.link, 'title':i.title, 'detail':i.detail} )
        return JsonResponse(p, safe=False)
    
class ListaNotificacionDia(View):
    def get(self, request, *args, **kwargs):
        dia_actual = datetime.now()
        
        notificacion = Notificacion.objects.filter(date=dia_actual).count()
        print(notificacion)
        if notificacion > 0:
            p = {'estado':True}
        else:
            p = {'estado':False} 
        return JsonResponse(p)
        

        
