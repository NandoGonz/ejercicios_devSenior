'''Crea una clase Contador que tenga un atributo de clase para contar cuántos objetos se han creado.'''
class Contador:
    cantidad = 0
    def __init__(self):
        Contador.cantidad += 1 

# Esta es la forma de instanciar lo objetos, cuando declaramos un atributo directamente en nuestra clase 
c1 = Contador()
print(Contador.cantidad)
c2 = Contador()
print(Contador.cantidad)
c3 = Contador()
print(Contador.cantidad)