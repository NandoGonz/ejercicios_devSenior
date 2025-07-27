'''Ejercicio 2: Conversor de Temperatura
Crea un programa que convierta grados Celsius a Fahrenheit usando la fórmula: F = (C × 9/5) + 32

Pide al usuario que ingrese la temperatura en Celsius
Convierte a Fahrenheit usando la fórmula
Muestra ambos valores'''

def conversor_temperatura(c):
    return (c * 9/5) + 32
print(f"La temperatura es de grados: {conversor_temperatura(50)} Fahrenheit")