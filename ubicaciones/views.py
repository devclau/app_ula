from django.shortcuts import render, HttpResponse
from django.db.models import Q, F
from ubicaciones.models import Categoria, Espacio
from django.db import connection
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
import json

class ListaUbicaciones(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        lista_edificacion=[]
        lista_direccion=[]
        lista_espacio=[]
        lista_funcion=[]
        lista_usabilidad=[]
        lista_usuario=[]
        lista_ciudad=[]
        # Seleccionar registros de las tablas 'depend', 'edifica' y 'sede' y combinarlos según la cláusula WHERE y ORDER BY
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT d.id_sede, s.nom_sede, d.id_edif, e.nom_edif FROM ubicaciones_dependencia d, view_edificacion e, view_sede s WHERE d.id_edif = e.id_edif AND d.id_sede = s.id_sede group by  d.id_sede, s.nom_sede, d.id_edif, e.nom_edif ORDER BY d.id_sede, e.nom_edif")
            edificacion = cursor.fetchall()
            for i in edificacion:
                lista_edificacion.append({'id_sede':i[0], 'nom_sede': i[1], 'id_edif':i[2], 'nom_edif':i[3]} )

            
            cursor.execute("select distinct d.id_sede, s.nom_sede, c.id_ciud, c.nom_ciud from ubicaciones_dependencia d, view_sede s, view_ciudad c where d.id_sede=s.id_sede and d.id_ciud=c.id_ciud and d.id_acceso =1")
            direccion = cursor.fetchall()
            for i in direccion:
                lista_direccion.append({'id_sede':i[0], 'nom_sede': i[1], 'id_ciud':i[2], 'nom_ciud':i[3]} )
            
            cursor.execute("select distinct d.id_sede, s.nom_sede, t.id_tesp, t.nom_tesp from ubicaciones_espacio e, ubicaciones_dependencia d, view_espacio t, view_sede s where e.id_dep= d.id_dep and e.id_esp= t.id_tesp and d.id_sede= s.id_sede order by d.id_sede, t.nom_tesp")
            espacio = cursor.fetchall()
            for i in espacio:
                lista_espacio.append({'id_sede':i[0], 'nom_sede': i[1], 'id_tesp':i[2], 'nom_tesp':i[3]} )

            cursor.execute("select distinct d.id_sede, s.nom_sede, f.id_func, f.nom_func from ubicaciones_espacio e, ubicaciones_dependencia  d, view_funcion f, view_sede s where e.id_dep= d.id_dep and e.id_func= f.id_func and d.id_sede= s.id_sede order by d.id_sede, f.nom_func")
            funcion = cursor.fetchall()
            for i in funcion:
                lista_funcion.append({'id_sede':i[0], 'nom_sede': i[1], 'id_func':i[2], 'nom_func':i[3]} )
            
            cursor.execute("select distinct d.id_sede, s.nom_sede, e.id_usab, u.nom_usab from ubicaciones_espacio e, ubicaciones_dependencia d, view_usabilidad u, view_sede s where e.id_dep= d.id_dep and e.id_usab= u.id_usab and d.id_sede= s.id_sede order by d.id_sede, u.nom_usab")
            usabilidad = cursor.fetchall()
            for i in usabilidad:
                lista_usabilidad.append({'id_sede':i[0], 'nom_sede': i[1], 'id_usab':i[2], 'nom_usab':i[3]} )

            cursor.execute("select distinct d.id_sede, s.nom_sede, e.id_usua, u.nom_usua from ubicaciones_espacio e, ubicaciones_dependencia d, view_usuario u, view_sede s where e.id_dep= d.id_dep and e.id_usua= u.id_usua and d.id_sede= s.id_sede order by d.id_sede, u.nom_usua")
            usuario = cursor.fetchall()
            for i in usuario:
                lista_usuario.append({'id_sede':i[0], 'nom_sede': i[1], 'id_usua':i[2], 'nom_usua':i[3]} )



            resultado=[lista_edificacion, lista_direccion,lista_espacio, lista_funcion, lista_usabilidad, lista_usuario]
            return JsonResponse(resultado, safe=False)
    
    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        lista=[]

        with connection.cursor() as cursor:
            if  "id_espc" in jd:
                id_espc =jd["id_espc"]
                id_sede = jd['id_sede']
                cursor.execute(f"select e.id_espc, e.nom_espc, e.id_nivel, d.longitud, d.latitud  from ubicaciones_espacio e, ubicaciones_dependencia d, view_espacio t, view_sede s where e.id_dep= d.id_dep  and  e.id_esp= t.id_tesp and d.id_sede= s.id_sede  and t.id_tesp={id_espc} and d.id_sede={id_sede} order by d.id_sede, e.nom_espc")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_espc':i[0], 'nom_esp': i[1], 'nivel':i[2], 'longitud':i[3], 'latitud':i[4]} )
            
            elif "id_ciud" in jd:
                id_sede =jd["id_sede"]
                id_ciud = jd['id_ciud']
                cursor.execute(f"select d.id_sede, s.nom_sede, c.id_ciud, c.nom_ciud, i.id_dire, i.nom_dire, d.longitud, d.latitud from ubicaciones_dependencia d, view_sede s, view_ciudad c, view_direccion i where d.id_sede= {id_sede} and d.id_ciud={id_ciud} and d.id_dire=i.id_dire and d.id_acceso=1 order by d.id_sede, c.nom_ciud, i.nom_dire")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_sede':i[0], 'nom_sede': i[1], 'id_ciud':i[2], 'nom_ciud':i[3], 'id_dire':i[4], 'nom_dire':i[5], 'longitud':i[6], 'latitud':i[7]} )
                    
            elif "id_edif" in jd:
                id_sede = jd['id_sede']
                id_edif  =jd['id_edif']
                cursor.execute(f"select d.id_sede, s.nom_sede, d.nom_dep, d.longitud, d.latitud from ubicaciones_dependencia d, view_sede s where d.id_sede=s.id_sede  and d.id_sede={id_sede}  and d.id_edif={id_edif} order by d.id_sede")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_sede':i[0], 'nom_sede': i[1], 'nom_dep':i[2], 'longitud':i[3], 'latitud':i[4]} )

            elif "id_func" in jd:
                id_sede = jd['id_sede']
                id_func  =jd['id_func']
                cursor.execute(f"select d.id_sede, s.nom_sede, e.nom_espc, e.id_nivel, d.longitud, d.latitud from ubicaciones_espacio e, ubicaciones_dependencia d, view_funcion f, view_sede s where e.id_dep=d.id_dep and e.id_func=f.id_func and d.id_sede=s.id_sede and e.id_func={id_func} and d.id_sede={id_sede} order by d.id_sede, e.nom_espc")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_sede':i[0], 'nom_sede': i[1], 'nom_espc':i[2], 'id_nivel':i[3], 'longitud':i[4],'latitud':i[5] } )

            elif "id_usab" in jd:
                id_sede = jd['id_sede']
                id_usab  =jd['id_usab']
                cursor.execute(f"select d.id_sede, s.nom_sede, e.id_espc, e.nom_espc, e.id_nivel, d.longitud, d.latitud from ubicaciones_espacio e, ubicaciones_dependencia d, view_usabilidad u, view_sede s where e.id_dep=d.id_dep and e.id_usab=u.id_usab and d.id_sede=s.id_sede and u.id_usab={id_usab} and d.id_sede={id_sede} order by d.id_sede, e.nom_espc")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_sede':i[0], 'nom_sede': i[1], 'id_espc':i[2] ,'nom_espc':i[3], 'id_nivel':i[4], 'longitud':i[5],'latitud':i[6] } )
            
            elif "id_usua" in jd:
                id_sede = jd['id_sede']
                id_usua  =jd['id_usua']
                cursor.execute(f"select d.id_sede, s.nom_sede, e.nom_espc, e.id_nivel, d.longitud, d.latitud from ubicaciones_espacio e, ubicaciones_dependencia d, view_usuario u, view_sede s where e.id_dep=d.id_dep and e.id_usua=u.id_usua and d.id_sede=s.id_sede and u.id_usua={id_usua} and d.id_sede={id_sede} order by d.id_sede, e.nom_espc")
                row = cursor.fetchall()
                for i in row:
                    lista.append({'id_sede':i[0], 'nom_sede': i[1], 'nom_espc':i[2], 'id_nivel':i[3], 'longitud':i[4],'latitud':i[5] } )

                      
        
        return JsonResponse(lista, safe=False)