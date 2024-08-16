#ejemplo del uso del map, filter y reduce:
from functools import reduce

listaNombres = ["Gabo","Sandoval","Camilo","Maigart","Pinzón","Apu"]

#map: mapea una funcion a los elementos de un objeo iterable
#obtener las longitudes de los nombres:

def longCadena(c):
    return len(c)

#obtener nueva lista con las longitudes de los nombres:
longitudes = list (map(longCadena, listaNombres))

#filtrar longitudes mayores a 5:
longitudes_mayores = list(filter(lambda n: n >=5 , longitudes))
print(longitudes_mayores)

#sumar todos los valores de la lista

long_totales = reduce(lambda x,y: x+y, longitudes)

print(listaNombres)
print(longitudes)
print(longitudes_mayores)
print(long_totales)
