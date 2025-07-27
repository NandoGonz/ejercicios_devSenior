'''Solicita el nombre de un estudiante y su nota final. Muestra si aprobó el curso (nota ≥ 3.0).'''

nombre_estudiante = input("ingresa el nombre del estudiante: ")
nota = float(input("ingrese la nota del estudiante: "))

if nota >= 3.0:
    print(F"La nota final del estduiente: {nombre_estudiante} es: {nota} por lo tanto aprobo")
else: 
    print(f"la nota fianl del estudiante: {nombre_estudiante} es {nota} por lo tanto reprobo ")    