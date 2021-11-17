# Ejercicio 1 prograam  que pregunte al usuario su nombre y edad y le muestre el años que cumplira los 100 años
from datetime import date
def preguntar_nombre():
    nombre = input("Cuál es tu nombre? ")
    print("Hola", nombre)
    return
def preguntar_edad():
    global var_edad
    var_edad = input("Cuál es tu edad? ")
    print("Tienes ",var_edad, " años")
    return

preguntar_nombre()
preguntar_edad()
#Obtenemos el año en que nacio
annoactual = date.today().year
anno_nacimiento = annoactual - int(var_edad)
print("Año en que naciste:" , anno_nacimiento)
cumplir_100 = anno_nacimiento + 100
print("Año en que cumpliras 100 años:" , cumplir_100)