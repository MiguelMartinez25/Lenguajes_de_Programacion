def get_movie_recommendations(genre):
    #base de datos como un diccionario con listas por cada género (llave):
    movies_db = {
        "action": ["Letal Weapon 4"," Die Hard 2","Mad Max Fury Road","The Dark Knight"],
        "sci-fi": ["2001: space odyssey","Interestellar","Planet of the apes","12 Monkeys","Brazil"],
        "animation": ["Toy Story","Wall-e","",""]
    }

    #definición de la lista que va a ser usada por el stream:
    recommendations = movies_db.get(genre,[])

    #productor perezoso:
    def recommendation_stream(index=0):
        if index < len(recommendations):
            yield recommendations[index]                    #head
            yield from recommendation_stream(index+1)       #tail

    return recommendation_stream()


genre = input("de qué genero desea ver recomendaciones? ")
stream_by_Genre = get_movie_recommendations(genre)

print(next(stream_by_Genre))
print(next(stream_by_Genre))
#print(next(stream_by_Genre))
#print(next(stream_by_Genre))

