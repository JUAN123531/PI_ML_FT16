from fastapi import FastAPI
import pandas as pd
# from recommendation import cosine_sim


app = FastAPI()


# 1


@app.get('/developer/')
def developer(desarrollador: str) -> int:
    ''' Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora'''
    df = pd.read_parquet(r'./Data/endpoint1.parquet.gzip')
    fil = df[df.year == year]
    items_count = len(df[df.item_id == item_id])
    return {
      'Año': fil, 
      'Cantidad de Items':items_count,
      'Contenido Free': fil.price.to_list()[0] * 100}

# 2


@app.get('/userdata/')
def userdata(user_id : str) -> dict:
    """
 Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
    """
    df = pd.read_parquet(r'./Data/endpoint2.parquet.gzip')
    user_data = df[df['user_id'] == user_id]

    # Calcula total gastado por usuario
    total_spent = user_data['price'].sum()
    
    total_items = user_data['items_count'].sum()

    
    # Calcula porcentaje de recomendaciones y total de reviews
    total_recommended = user_data['reviews_recommend'].sum()
    total_reviews = user_data.shape[0]
    recommendation_percentage = (total_recommended / total_reviews) * 100

    return {
        'Usuario': user_id,
        'Dinero gastado': total_spent,
        'Porcentaje de recomendaciones': recommendation_percentage,
        'cantidad de items': total_items
      
    }


# 3


@app.get('/UserForGenre/')
def UserForGenre(genero : str ):
    """
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    """
    df = pd.read_parquet(r'./Data/endpoint3.parquet.gzip')
    # Verifica si el genero ingresado existe en el DataFrame
    if genero not in df.columns:
        return "Invalid genre"
     # Multiplica la columna del genero por la columna de playtime_forever
    genre_playtime = df[genre] * df['playtime_forever']
    
    # Calcula el total de horas jugadas en el genero
    total_genre_playtime = genre_playtime.sum()

    # Lista de generos pertenecientes al DataFrame
    genre_columns = [
        'Action', 'Indie', 'Adventure', 'Casual', 'Fighting', 'Multiplayer',
        'Puzzle', 'RPG', 'Sandbox', 'Shooter', 'Simulation', 'Singleplayer',
        'Sports', 'Strategy', 'Survival', 'Zombies'
    ]

    # Calcula el total de horas jugadas en cada genero
    total_playtimes = {
        genre: (df[genre] * df['playtime_forever']).sum()
        for genre in genre_columns
    }

    # Ordena los generos de mayor a menor
    sorted_genres = sorted(total_playtimes.items(),
                           key=lambda x: x[1],
                           reverse=True)

    # Busca el puesto del genero ingresado
    rank = 1
    for genre, playtime in sorted_genres:
        if genre == genre:
            return rank
        rank += 1
    # Filtra el DataFrame por el genero ingresado
    genre_df = df[df[genero] == 1]

    # Ordera el DataFrame por playtime_forever
    sorted_genre_df = genre_df.sort_values(by='playtime_forever',
                                           ascending=False)

    # Extrae los primeros 5 usuarios
    top_5 = sorted_genre_df.head(1)

    # Crea un diccionario con los usuarios y sus datos
    top_users_dict = {}
    for _, row in top_5.iterrows():
        top_users_dict[row['user_id']] = {
            'user_url': row['user_url_x'],
            'playtime_forever': row['playtime_forever']
        }

    return {
      "Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
       "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
   
# 4


@app.get('/best_developer_year/')
def  best_developer_year(año : int):
    """
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    df = pd.read_parquet(r'./Data/endpoint4.parquet.gzip')
    fil = df['reviews_recommend','reviews_helpful','reviews_review']
    return {
        'Puesto 1': fil.reviews_recommend.count(),
        'Puesto 2': fil.reviews_review.count(),
        'Puesto 3': fil.reviews_helpful.count()
    }

# 5

# @app.get('/developer_reviews_analysis/')
# def developer_reviews_analysis(desarrollador : int) -> dict:
#     """
#    Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo
#     """
#     df = pd.read_parquet(r'./Data/endpoint5.parquet.gzip')
#     fil = df[df.year == year]
#     Negative= 
#     Positive =
#     return {
#         'Valve' : [Negative = 182, Positive = 278]
    # }
# ML
# @app.get('/recomendacion_juego/{id_del_producto}')
# def recomendacion_juego(id_del_producto: str):
#      ''' 
#      Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
#       '''
#     games_model= pd.read_parquet(r'./Data/endponint6_with_reco.parquetparquet.gzip')
#     #def recomendacion_juego( id de producto ): Ingresando el id de producto,
#     # deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
#     item_indice = games_model[games_model['id'] == id_del_producto].index[0] # Extraemos el indice de nuestro juego en nuestro dataset de juegos
#     items_similares = list(enumerate(cosine_sim[item_indice])) # Conseguimos nuestros items similares
#     recommended_items = sorted(items_similares, key=lambda x: x[1], reverse=True) # Ahora ordenamos para saber nuestros items mas recomendados
#     indices = [index for index, _ in recommended_items[1:10]] # Extraemos los indices de los juegos
#     recommended_items = games_model.iloc[indices]['id'].tolist() # Convertimos a listas con nuestros ids, (podriamos poner nuestros app_name)
#     recomedations = ""
#     for i in recommended_items[:5]:
#         recomedations+=f'<p>{games_model[games_model.id == i].app_name.tolist()[0]}</p>'
    # return recomedations # Retornamos los primeros 5



