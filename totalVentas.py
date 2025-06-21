'''Solicita la cantidad de productos vendidos y el precio unitario, luego muestra el total de ventas.'''
productos_vendidos = int(input("ingrese la canridad de productos vendidos: "))
total_ventas = 0
for productos in range(productos_vendidos):
    precio_producto = float(input("ingrese el valor del producto: "))
    total_ventas += precio_producto
print(f"la venta total es de: {total_ventas}")    