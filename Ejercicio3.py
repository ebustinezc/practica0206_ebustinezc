# Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, 
# pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio 
# de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje 
# informando de ello.

# Producto  Precio
# Pan       1.40
# Huevos    2.30
# Cebolla   0.85
# Aceite    4.35

precios  = {"Pan":1.40 , "Huevos":2.30 , "Cebolla":0.85 , "Aceite":4.35}
producto = input("Dime el producto ")
cantidad = int(input("Dime la cantidad "))
if producto in precios:
    print(cantidad, 'de', producto, 'valen', precios[producto]*cantidad, '€')
else: 
    print("No esta disponible ")