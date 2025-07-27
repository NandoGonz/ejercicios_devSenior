'''Solicita el nombre de una ciudad y la temperatura actual, luego muestra si hace frío (≤18°C), calor (≥30°C) o clima templado.'''

nombre_de_la_ciudad = input("escriba el nombre de su ciudad: ")
temp_de_la_ciudad = float(input("ingrese la temperatura de la ciudad: "))

if temp_de_la_ciudad <= 18:
    print(f"la temperatura de la ciudad {nombre_de_la_ciudad} es de: {temp_de_la_ciudad}°C hace frio ")
elif temp_de_la_ciudad >= 30:
    print(f"la temperatura de la ciudad {nombre_de_la_ciudad} es de: {temp_de_la_ciudad}°C hace calor")    
else:
    print(f"la tesperatura de la cidad {nombre_de_la_ciudad} es de: {temp_de_la_ciudad} hace un clima agradable")    
    