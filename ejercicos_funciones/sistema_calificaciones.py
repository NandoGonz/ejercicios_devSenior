'''Desafío: Sistema de Calificaciones
Crea un programa que calcule el promedio de calificaciones de un estudiante y determine su nivel de rendimiento.

Pide al estudiante que ingrese 5 calificaciones (0-100)
Calcula el promedio de las calificaciones
Determina el nivel de rendimiento según el promedio:
• 90-100: Excelente
• 80-89: Muy Bueno
• 70-79: Bueno
• 60-69: Regular
• 0-59: Necesita Mejorar
Muestra el promedio y el nivel de rendimiento

calificaciones = 0

for i in range(5):
    calificacion = float(input("Ingrese la calificación: "))
    calificaciones += calificacion
    
promedio = calificaciones / 5
if 90 <= promedio <= 100:
    print(f"Su rendimiento es: {promedio:.1f} Excelente")
elif 80 <=  promedio <= 89:
    print(f"Su rendimiento es: {promedio:.1f} muy Bueno")
elif 70 <=   promedio <= 79:
    print(f"Su rendimiento es: {promedio:.1f} Bueno")
elif 60 <=  promedio <= 69:
    print(f"Su rendimiento es: {promedio:.1f} Regular")
else:
    print(f"Su rendimiento es: {promedio:.1f} necesitas mejorar")'''
    
# Usando return

    

def rendimiento_alumno(promedio):
    if 90 <= promedio <= 100:
        return f"Su rendimiento es: {promedio:.1f} Excelente"
    elif 80 <=  promedio <= 89:
        return f"Su rendimiento es: {promedio:.1f} muy Bueno"
    elif 70 <=   promedio <= 79:
        return(f"Su rendimiento es: {promedio:.1f} Bueno")
    elif 60 <=  promedio <= 69:
        return f"Su rendimiento es: {promedio:.1f} Regular"
    else:
        return f"Su rendimiento es: {promedio:.1f} necesitas mejorar"


calificaciones = 0

for i in range(5):
    calificaion = float(input("Ingrese la calificación: "))
    calificaciones += calificaion
    
promedio = calificaciones / 5
resultado = rendimiento_alumno(promedio)
print(resultado)