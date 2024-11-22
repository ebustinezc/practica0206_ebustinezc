# Escribir un programa que guarde en una variable 
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo 
# o un mensaje de aviso si la divisa no está en el diccionario.

Moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
Usuario = input("Introduce una moneda ")
if Usuario.title() in Moneda:
    print(Moneda[Usuario.title()])
else:
    print("La moneda no esta")