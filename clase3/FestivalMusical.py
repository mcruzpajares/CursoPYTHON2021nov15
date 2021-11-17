# Ejemplo de clase y creación de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # Inicializa los parámetros
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
    def festival_metodo(self):
        print("El mejor festival es: ")

# Se crea una instancia de la clase FestivalMusical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')
festival2 = FestivalMusical('Primavera Sound', 'SP', 'Dance')
# Se accede a los atributos del objeto
print('Nombre festival:', festival1.nombre)
# Muestra la posición del objeto de la clase FestivalMusical en la memoria
print(festival1)
# LLamamos al metodo
festival1.festival_metodo()

print(festival1.nombre.upper())
festival2.nombre = ('Benicassim')

print(festival2.nombre.upper())


