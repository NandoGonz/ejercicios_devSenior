'''Crea un programa que verifique si una contraseña cumple con los requisitos básicos de seguridad.

La contraseña debe tener al menos 8 caracteres
Debe contener al menos una letra mayúscula
Debe contener al menos un número
Muestra si la contraseña es válida o no


password = input("Ingrese una contraseña: ")
# Veificamos la longitud
longitud = len(password) <= 8
# Verificamos si tiene mayusculas 
tiene_mayuscula = False

for letra in password:
    
    if letra.isupper():
        tiene_mayuscula = True
        break
# verificamos si tiene numero 
tiene_digito = False 

for letra in password:
    
    if letra.isdigit():
        tiene_digito = True
        break 

# Verificamos la valides de la contraseña

validar = longitud and tiene_mayuscula and tiene_digito
print(f"La contraseña es valida?! : {validar} ")'''

# Uso practico del return

'''def doble(num):
    doblador = num * 2 
    return doblador
print(f"El doble es {doble(5)}")'''
# Desarrollare el mismo ejercico con el uso de una función 

def verificar_password(contrasena):

    mayuscula = False
    digito = False
        
    for letra in contrasena:
        if letra.isupper():
            mayuscula = True

    for letra in contrasena:
        if letra.isdigit():
            digito = True
        
    longitud = len(contrasena) <= 8
    return mayuscula and digito and longitud
contrasena = input("Ingrese la contraseña: ")
verificacion = verificar_password(contrasena)

if verificacion:
    print("La contraseña es valida")
    
else:
    print("La contraseña es invalida")
    
