'''Ejercicio 4: Calculadora de Descuento
Crea un programa que calcule el precio final de un producto después de aplicar un descuento.

Pide el precio original del producto
Pide el porcentaje de descuento
Calcula el precio con descuento
Muestra el precio original, descuento y precio final
# Función sin parametros

def descuento():
    precio_org = float(input("Ingrese el valor del producto: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje a descontar: "))
    descontar = precio_org * porcentaje_descuento
    total_pagar = precio_org - descontar
    
    if precio_org > 200000:
        print(f"el precio de la compra es de: {precio_org} y tiene un descuento de: {descontar} deb pagar {total_pagar}")
    else:
        print(f"Su compra es de: {precio_org} no tiene ningun descuento")

descuento()'''

''' Función con parametros
def calcular_descuento(precio_inicial, porcentaje__descontar):
    aux_descuento = precio_inicial * (porcentaje__descontar / 100)
    pago_total = precio_inicial - aux_descuento
    
    
    if precio_inicial > 200000:
        print(f"Su compra es de {precio_inicial} y tiene un descuento de: {aux_descuento}, debe pagar un total de: {pago_total}")
    
    else:
        print(f"Su compra es de: {precio_inicial} no tiene ningun descuento")

precio = float(input("Ingrese el valor de la compra: "))
porcentaje_descuento = float(input("Ingrese el porcentaje que desea descontar: "))
calcular_descuento(precio, porcentaje_descuento) '''

# Fucnion con return

def calcular_descu(p_inicial,porcentaje_des):
    '''Usamos un condicional para establecer el valor apartir del cual se daran los descuentos'''
    
    if p_inicial > 200000:
        descuento = p_inicial * (porcentaje_des / 100)
        total_pagar = p_inicial - descuento
        return total_pagar
    else:
        return p_inicial
# Entrada de datos y llamado a la función 
valor = float(input("Ingrese el monto a pagar: "))
para_descontar = float(input("Ingrese el porcentaje para el descuento: "))
total_pago = calcular_descu(valor, para_descontar)

# Mostramos el resultado
if valor > 200000:
    print(f"🎉 Has obtenido un descueto, total a pagar: {total_pago}")
else:
    print(f"🥹 No tiene descuetno debe cancelar: {total_pago}")