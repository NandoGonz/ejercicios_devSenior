'''Pide el nombre de un proyecto y los días estimados de duración, luego muestra cuántas semanas tomará (redondeando hacia arriba)'''

nombre_proyecto = input("ingrese el nombre de su proyecto: ")
dias_de_duracion = int(input("ingrese los dias que durara el proyecto: "))
semanas_de_duracion = (dias_de_duracion + 6) // 7 
print(f"la cantidad de semanas que se empleara en este proyecto es de: {semanas_de_duracion } semanas")
