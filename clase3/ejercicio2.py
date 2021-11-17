# Ejercicio2 Preguntar al usuario un número y mostrar si es par o impar. Si el número es múltiple de 4 imprimir el mensaje apropiado al usuario.
def preguntar_numero():
    global var_numero
    var_numero = input("Introduzca un numero? ")
    return


preguntar_numero()
if int(var_numero) % 2 == 0:
    print(var_numero, ' es par')
    if int(var_numero) % 4 == 0:
        print(var_numero, ' es multiplo de 4')
else:
    print(var_numero, ' es impar')
