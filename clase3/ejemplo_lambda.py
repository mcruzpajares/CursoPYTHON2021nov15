# Ejemplo función lambda
multiplicar = lambda x, y: x * y
print(multiplicar(5, 5))

print(f'{(lambda x: x*5)(5)}')

print(f'{(lambda x, y: x * y)(5, 5)}')

