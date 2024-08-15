# Listas de datos
videogames = []
publishers = []
users = [] 
reviews = []

def addUser(id, username, country, age):
    newUser = {"id": id, "username": username, "country": country, "age": age}
    users.append(newUser)

def addVideogames(id, name, genre, year, downloads, awarded):
    newVideogame = {"id": id, "name": name, "genre": genre, "year": year, "downloads": downloads, "awarded": awarded}
    videogames.append(newVideogame)

def addPublishers(id, name, country, tot_sales):
    newPublisher = {"id": id, "name": name, "country": country, "tot_sales": tot_sales}
    publishers.append(newPublisher)

def filter_list(data_list, filters, operator='and'):
    """
    Filtra una lista de diccionarios basado en criterios dinámicos.

    :param data_list: Lista de diccionarios a filtrar.
    :param filters: Diccionario de condiciones de filtro.
    :param operator: 'and' para que todos los filtros sean verdaderos, 'or' para al menos uno.
    :return: Lista filtrada.
    """
    if operator == 'and':
        # Usamos 'all' para asegurarnos de que todos los filtros se cumplan
        return [item for item in data_list if all(item.get(k) == v for k, v in filters.items())]
    elif operator == 'or':
        # Usamos 'any' para que al menos un filtro se cumpla
        return [item for item in data_list if any(item.get(k) == v for k, v in filters.items())]
    else:
        raise ValueError("El operador debe ser 'and' o 'or'.")

# Ejemplo de uso para videojuegos
addVideogames(1, "Game A", "Action", 2020, 1500, True)
addVideogames(2, "Game B", "Adventure", 2021, 900, False)
addVideogames(3, "Game C", "Action", 2019, 2500, True)

# Filtros dinámicos
filters = {'genre': 'Action', 'downloads': 1500}
videogames_filtered = filter_list(videogames, filters, operator='and')

for game in videogames_filtered:
    print(f"ID: {game['id']}, Name: {game['name']}, Downloads: {game['downloads']}")

# Ejemplo de uso para usuarios
addUser(1, "user1", "USA", 25)
addUser(2, "user2", "Canada", 30)
addUser(3, "user3", "USA", 22)

# Filtros dinámicos para usuarios
user_filters = {'country': 'USA'}
users_filtered = filter_list(users, user_filters, operator='or')

for user in users_filtered:
    print(f"ID: {user['id']}, Username: {user['username']}, Country: {user['country']}")
