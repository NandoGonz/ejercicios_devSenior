"""Este es el inventario con el que estare trabajando"""

inventario = [["leche", 20, 3500.0], ["pan", 50, 2000.0], ["huevos", 30, 500.0]]


def menu():
    """Este metodo muestra todas funcionalidades del programa"""
    print("1. Ver el inventario")
    print("2. Registrar la venta de un producto")
    print("3. Actualizar los productos en el inventario")
    print("4. Agregar un nuevo producto a el inventario")
    print("0. Salir del menú")


def ver_inventario():
    """Este metodo mustra el inventario"""
    for producto in inventario:
        print("Productos en el inventario")
        print(
            f"Producto: {producto[0]}-----> Cantidad: {producto[1]}-----> Valor: {producto[2]}"
        )


def registrar_venta():
    """Este metodo registra la venta y en el inventario"""
    articulo = input("Ingrese el proucto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender del articulo: "))
    for producto in inventario:

        if producto[0] == articulo:
            producto[1] -= cantidad
            print("✅ Venta realizada con exito")

            break
    else:
        print("❌ El producto que busca no ha sido encontrado en inventario")


def actualizar_inventario():
    """Este metodo"""
    articulo = input("Ingrese el nombre del producto que desea actualizar: ")
    cantidad = int(input("Ingrese la cantidad a incrementar del articulo: "))
    for producto in inventario:

        if producto[0] == articulo:
            producto[1] += cantidad
            print("✅ Se ha actualizado el producto de forma correcta")
            break
    else:
        print("❌ El producto que busca no ha sido encontrado en inventario")


def nuevo_producto():
    """Este metodo regidtra un nuevo producto en el inventario"""
    n_producto = input("Nombre del nuevo producto: ")
    cantidad_producto = int(
        input("Ingrese la cantidad de unidades del nuevo producto: ")
    )
    precio_producto = float(input("Ingrese el valor del nuevo prodicto: "))
    nuevo_articulo = [n_producto, cantidad_producto, precio_producto]
    inventario.append(nuevo_articulo)
    print("✅Se ha registrado el nuevo producto de forma correcta")


def main():
    """Este metodo es el controlador el timon de todo el programa"""
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    ver_inventario()

                case 2:
                    registrar_venta()

                case 3:
                    actualizar_inventario()

                case 4:
                    nuevo_producto()

                case 0:
                    print("🎉 GRACIAS POR USAR EL NUESTRO IVENTARIO")
                    print("📤 Esta saliendo del menu del inventario")
                    break

        except ValueError:
            print("Ingrese un valor correcto")


if __name__ == "__main__":
    main()
