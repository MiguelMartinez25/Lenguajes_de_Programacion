Funciones de orden superior:
-MAP: Mapea una función [a cada elemento de una lista iterable], generando una nueva colección.
-FILTER: Aplica una función booleana [*], más pequeña que la colección generada en la función MAP.
-REDUCE: Consolida los elementos de un iterabe, en un solo valor, usando un operador o una función.

from functools import reduce

secuencias_adn = [ "ATCGATCGA", "GGTACGTA", "CAGTTGCA", "GCGCGCGCGC", "AATTCCGG", "TTAAACCGG", "GGATCGATCG" ]

longitudes = list(map(lambda s: len(s),secuencias_adn))

def porcentajeA(secuencias_adn):
    totalCaracateres = len(secuencias_adn)
    letra = secuencias_adn.count("A")
    porcentaje = (letra/totalCaracateres)*100
    return porcentaje
porcentaje_A = list(map(porcentajeA, secuencias_adn))
print(f"RESULTADO DE APLICAR MAP SOBRE LA LISTA Y CALCULAR EL PORCENTAJE DE 'A' EN CADA CADENA: \n{secuencias_adn}: \n{porcentaje_A}")

porcentajeMayor = list(filter(lambda s: porcentajeA(s)>25 , secuencias_adn))
print(f"CADENAS CUYO PORCENTAJE ES MAYOR AL 25% DE 'A': \n{porcentajeMayor}")

concatenarFiltered = reduce(lambda x,y: x+y, porcentajeMayor)
cantidadTotal = len(concatenarFiltered)
print(f"SECUENCIA FINAL Y SU LONGITUD: \n{concatenarFiltered} \n{cantidadTotal}")
