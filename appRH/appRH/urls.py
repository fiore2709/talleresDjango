from django.contrib import admin
from django.urls import path
###from webApp.views import mensaje, tabla, calculo_de_datos

# ###urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('mensaje/', mensaje),
#     path('informeproducto/', tabla),
#     path('calculoedad/<int:anio>',calculo_de_datos)
#     path('',inicio, name='inicio'),####
from django.urls import path
from webApp.views import index,informes,formulario

urlpatterns = [
    path('', index, name='index'),
    path('informes/', informes, name='informes'),
    path('formulario/', formulario, name='formulario'),
]
