'''Pide el número de participantes en un evento y muestra si se superó el cupo máximo de 100 personas.'''

participantes = int(input("ingrese en numero de participantes: "))
cupos = 100
plazasDisponibles = cupos - participantes
if participantes > cupos:
   
    print(f"la cantidad de participantes es: {participantes} supera nuestra capacidad de {cupos} personas")
else:
    print(f"la cantidad de participantes es: {participantes} aun tenemos capacidad de {plazasDisponibles} personas ")    