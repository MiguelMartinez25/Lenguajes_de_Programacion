#print("Hola mundo")
#nombre = input ("Ingrese su nombre ")
#print(f"su nombre es {nombre}")
#-------------------Notas-------------------------
#Funciones Puras => a)no tiene efectos colaterales 
# (relacionado con la "inmutabilidad"). 
# b)con las mismas entradas produce las mismas salidas

videogames = []
publishers = []
users = []
reviews= [] 

def addVideogame(id, name, genere, year, downloads, awarded):
    newVideogame = {"id":id, "name":name, "genere":genere, "year":year, "downloads":downloads, "awarded":awarded}
    videogames.append(newVideogame)


def addPublisher(id, name, country, tot_sales):
    newPublisher = {"id":id, "name":name, "country":country, "tot_sales":tot_sales}
    publishers.append(newPublisher)


def addUser(id, username, country, age):
    newUser = {"id":id, "username":username, "country":country, "age":age}
    users.append(newUser)


def filterVideogames2(numDownloads):
    lista_filtrada = []
    for r in videogames:
        if r["downloads"] == numDownloads:
            lista_filtrada.append(r)
    return lista_filtrada
    
#result = filterVideogames2(videogames, lambda r: r["downloads"] == numDownloads)
#Filtrar por número de descargas

#result = filterVideogames(videogames, lambda r: r["name"] == "Crash")
#Filtrar por nombre del videojuego

#result = filterVideogames(videogames, lambda r: 1000 <= r["downloads"] <= 5000)
#Filtrar por un rango de descargas

def filter_downloads(videogame):
    return videogame["downloads"]>1000

videogames_filtered = list (filter(filter_downloads, videogames))

def filterPublisherByTotalSales_iter(totalSales):
    filteredList = []
    for rec in publishers:
        if rec["total_sales"] == totalSales:
            filteredList.append(rec)

    return filteredList


#Usando la función de orden superior "filter" y una función lambda de filtrado:
def filterPublisherByTotalSales_FilterLambda(totalSales, country, publishers):

    #def filterFunction1(rec, total_sales):
        #return rec["total_sales"] == totalSales
    #funcion de filtrado:
    #se aplica sobre cada elemento de la lista, que es un diccionario
    #de cada elemento, miro si la llave total_sales corresponde al parámetro
    filterFunction2 = lambda x: x["total_sales"] == totalSales and x["Country"] == country
    filteredList = list (filter(filterFunction2, publishers))
    return filteredList

#EJERCICIO: implementar filtrado por total de ventas y país
