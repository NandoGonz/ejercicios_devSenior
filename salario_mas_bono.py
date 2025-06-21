'''Pide el salario base de un empleado y calcula su salario total con un bono del 15%'''
nombre_empleado = input("ingrese el nombre del empleado: ")
salario = float(input("ingrese el salario: "))
bono = 0.15 * salario
salario_total = salario + bono
print(f"el salario de trabajador: {nombre_empleado} es: {salario_total}")
