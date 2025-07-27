'''Crea una clase Persona con los atributos nombre y edad. Instancia dos personas y muestra sus datos'''
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    '''Agrega un método saludar() a la clase Persona que imprima "Hola, soy [nombre]'''
    def saludar(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")


# Esta es la forma de mostrar por pantalla la instancia de nuestros objetos, cuando no agregamos un print en los atributos de la clase
'''persona1 = Persona("Luis", 29)
persona2 = Persona("Adriana", 30)
print(persona1.name, persona1.age)
print(persona2.name, persona2.age)'''

# Instanciaremos nuestros ob jetos usando nuestra clse y el metodo creado 
persona1 = Persona("Luis", 29)
persona1.saludar()
persona2 = Persona("Adriana", 30)
persona2.saludar()