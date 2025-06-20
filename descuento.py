'''Pide el nombre de un cliente y el monto de su compra, luego muestra si aplica a un descuento (si la compra es mayor a $500.000).'''

nombreCliente = input("Ingrese el nombre del cliente: ")
valorCompra = float(input("ingrese el valor de la compra: "))
descuento = valorCompra * 0.10
valoreApagar = valorCompra - descuento

if valorCompra > 500000:
    print(f"su compra es de {valorCompra} y tiene un descuento de {descuento} debe pagar {valoreApagar}")
else:
    print(f"su compra es de {valorCompra} debe pagar {valorCompra} no tiene ningun descuento")    