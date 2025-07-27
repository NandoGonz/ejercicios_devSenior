'''Crea una clase Cuenta con un atributo privado __saldo. Implementa métodos para depositar y retirar dinero, validando que el saldo nunca sea negativo.'''
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    
    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
    
    def mostrar_saldo(self):
        print(f"El saldo actual es {self.__saldo}") 

cuentaAhorro = Cuenta(300)
cuentaAhorro.depositar(45)
cuentaAhorro.retirar(140)
cuentaAhorro.mostrar_saldo()
