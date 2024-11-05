# import datetime
#
# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def mensaje (request):
#     return HttpResponse(f"<h1>Hola mundo, este es mi primer site</h1>")
#
# def tabla (request):
#     ProductoA= "Papitas rufles"
#     ProductoB= "Fideos instantaneos"
#     ProductoC= "Chocolate"
#     ProductoD= "Canela"
#     return HttpResponse(f"""
# <head>
#
#     <style>
#         table {{
#             width: 50%;
#             border-collapse: collapse;
#             margin: 20px 0;
#         }}
#         th, td {{
#             border: 1px solid black;
#             padding: 8px;
#             text-align: left;
#         }}
#         th {{
#             background-color: #f2f2f2;
#         }}
#     </style>
# </head>
# <body>
#
#     <h2>Listado de Productos</h2>
#
#     <table>
#         <thead>
#             <tr>
#                 <th>Descripción</th>
#                 <th>Precio</th>
#                 <th>Stock</th>
#                 <th>Estado</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
#                 <td>{ProductoA}</td>
#                 <td>$10.00</td>
#                 <td>50</td>
#                 <td>Disponible</td>
#             </tr>
#             <tr>
#                 <td>{ProductoB}</td>
#                 <td>$15.50</td>
#                 <td>20</td>
#                 <td>Disponible</td>
#             </tr>
#             <tr>
#                 <td>{ProductoC}</td>
#                 <td>$8.75</td>
#                 <td>0</td>
#                 <td>Agotado</td>
#             </tr>
#             <tr>
#                 <td>{ProductoD}</td>
#                 <td>$12.30</td>
#                 <td>5</td>
#                 <td>Disponible</td>
#             </tr>
#         </tbody>
#     </table>
#
# </body>
#     """)
#
# def calculo_de_datos (request, anio):
#     edad_actual= datetime.datetime.now().year-anio
#     return HttpResponse(f"<h1>Su edad es: {edad_actual}</h1>")

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def informes(request):
    informes = [
        {'id': 1, 'nombre': 'Juan Pérez', 'posicion': 'Analista', 'departamento': 'Finanzas', 'fecha_ingreso': '2021-05-12'},
        {'id': 2, 'nombre': 'Ana Gómez', 'posicion': 'Gerente', 'departamento': 'Recursos Humanos', 'fecha_ingreso': '2020-08-25'},
        # Agrega más registros según sea necesario
    ]
    return render(request, 'informes.html', {'informes': informes})

def formulario(request):
    if request.method == 'POST':
        # Aquí se maneja la lógica para el formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
        # Guardar o enviar datos según la lógica requerida
        return render(request, 'formulario.html', {'mensaje': 'Gracias por contactarnos.'})
    return render(request, 'formulario.html')
