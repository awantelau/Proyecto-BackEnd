from django.shortcuts import render

def inicio(request):
    return render(request, 'dispositivos/inicio.html')

def panel_dispositivos(request):

    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]
    
    consumo_maximo = 100
    criticos = 0  

  
    for dispositivo in dispositivos:
        if dispositivo['consumo'] > consumo_maximo:
            dispositivo['estado'] = 'Exceso'
            criticos += 1
        else:
            dispositivo['estado'] = 'Correcto'

    contexto = {
        'dispositivos': dispositivos,
        'consumo_maximo': consumo_maximo,
        'criticos': criticos,
    }
    
    return render(request, 'dispositivos/panel.html', contexto)