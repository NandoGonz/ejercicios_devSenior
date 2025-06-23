'''Solicita el puntaje de dos exámenes y muestra si el estudiante mejoró, empeoró o mantuvo su rendimiento.'''

nota_exam_1 = float(input("ingrese la nota del primer examen: "))
nota_exam_2 = float(input("ingrese la nota del segundo examen: "))

if nota_exam_1 > nota_exam_2:
    print(f"la nota del examen 1 es: {nota_exam_1} > a la nota del examen 2: {nota_exam_2} por lo tanto su rendimiento empeoro ")
elif nota_exam_1 < nota_exam_2:    
    print(f"la nota del examen 1 es: {nota_exam_1} < a la nota del examen 2: {nota_exam_2} por lo tanto su rendimiento mejoro ")
else: 
    print(f"la nota del examen 1 es: {nota_exam_1} es igual a la nota del examen 2 {nota_exam_2} por lo tanto mantuvo su rendimiento")    

        