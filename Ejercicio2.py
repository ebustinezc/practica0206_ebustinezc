# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
# “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”

diccionario ={}
diccionario["Nombre"]    = input("Cual es tu nombre")
diccionario["edad"]      = input("Que edad tienes")
diccionario["direccion"] = input("Donde vives")
diccionario["telefono"]  = input("Cual es  tu telefono")
print(diccionario['Nombre'], 'tiene', diccionario['edad'], 
      'años, vive en', diccionario['direccion'], 'y su número de teléfono es', diccionario['telefono'])
