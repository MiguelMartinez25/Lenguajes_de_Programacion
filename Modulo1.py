#print("Hola mundo")
#nombre = input ("Ingrese su nombre ")
#print(f"su nombre es {nombre}")

videogames = []  #listas
publishers = []
users = [] 
reviews = []

def addUser(id, username, country, age):
    newUser = {"id":id, "username":username, "country":country, "age":age}
    users.append(newUser)

def addVideogames(id, name, genre, year, downloads, awarded):
    newVideogame = {"id":id, "name":name, "genre":genre, "year":year, "downloads":downloads, "awarded":awarded}
    videogames.append(newVideogame)

def addPublishers(id, name, country, tot_sales):
    newPublisher = {"id":id, "name":name, "country":country, "tot_sales":tot_sales}
    publishers.append(newPublisher)

def filterVideogames2(numDownloads):
    lista_filtrada = []
    for r in videogames:
        if r["downloads"] == numDownloads:
            lista_filtrada.append(r)
    return lista_filtrada

def filter_downloads(videogame):
    return videogame["downloads"] > 1000
videogames_filtered = list (filter(filter_downloads, videogames))