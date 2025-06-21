'''Pide el nombre de una empresa y el año de fundación, luego muestra cuántos años lleva en funcionamiento'''
año_de_creacion = int(input("ingrese el año en que se fundo la empresa: "))
año_actual = int(input("ingrese el año actual: "))
años_en_funcionamiento = año_actual - año_de_creacion
print(f"la empresa lleva {años_en_funcionamiento} en funcionamiento")