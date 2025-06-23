'''Pide el número de horas trabajadas y la tarifa por hora, luego calcula el salario total.'''
horas_trabajadas = int(input("ingrese la cantidad de horas trabajadas: "))
pago_por_hora = float(input("ingrese el costo de una hora de trabajo: "))
salario_total = horas_trabajadas * pago_por_hora

print(f"su pago por las {horas_trabajadas} horas trabajadas es de: ${salario_total}")