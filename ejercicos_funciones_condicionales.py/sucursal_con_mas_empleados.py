'''Pide el número de empleados de dos sucursales y muestra cuál tiene más personal'''

sucursal_1 = int(input("ingrese la cantidad de empleados de la sucursal 1: "))
sucursal_2 = int(input("ingrese laa cantidad de empleados de la sucursal 2: "))

if sucursal_1 > sucursal_2:
    print(f"la sucursal 1 tiene mas empleados {sucursal_1}")
else:
    print(f"la sucursal 2 tiene mas empleados {sucursal_2}")    