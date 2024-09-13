"""
def cuenta_regresiva(n):
    while n > 0:
        yield n
        n -= 1
gen = cuenta_regresiva(3)

while True:
    try:
        print(next(gen))
    except StopIteration:
        print("Fin de la cuenta regresiva")
        break
"""
"""
def generador_pares():
    n = 0
    while True:
        if n % 2 == 0:
            yield n
        n +=1

gen = generador_pares()

try:
    for _ in range (5):
        print(next(gen))

    for _ in range(3):
        print(next(gen))
except StopIteration:
    print("Generador agotado")
finally:
    print("Fin de la iteración")
"""
"""
from functools import reduce
numeros = [1,2,3,4,5]
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado)
"""
"""
nums = [1,2,3,4]
incremento = lambda x: x + 1
resultado = list(map(incremento, filter(lambda x: x % 2 == 0, nums)))
print(resultado)
"""
"""
nums = [[1,2,3],[4,5,6]]
suma_interna = lambda lst: list(map(lambda x: x + 1, lst))
resultado = list(map(suma_interna, nums))
print(resultado)
"""