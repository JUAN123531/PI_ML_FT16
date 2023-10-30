<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

 

<hr>  

## Contenido del README

- [Descripción del Problema](#descripción-del-problema)
- [Contexto y desarrollo](#Contexto-y-desarrollo)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-(EDA))
- [Modelo de Aprendizaje Automático](#modelo-de-aprendizaje-automático)
- [Desarrollo de la API](#Desarrollo-de-la-API)
- [Transformaciones](#Transformaciones)
- [Video de Demostración](#video-de-demostración)
- [Repositorio](#repositorio)
- [Fuentes de Datos](#fuentes-de-datos)

## Descripción del Problema

Steam necesitaba un sistema de recomendación de videojuegos para sus usuarios. Los datos iniciales eran desafiantes, con datos crudos y poco limpios. Como MLOps Engineer se realizaron tareas de Data Engineering y se creo un MVP para abordar este problema, ademas de otras funciones.
## Contexto y desarrollo

Este proyecto de Machine Learning contempla desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

## Exploratory Data Analysis (EDA)

Se ha realizado un análisis exploratorio de datos para comprender mejor el dataset, incluyendo:

- Identificación de relaciones entre variables.
- Identificación de outliers o anomalías.
- Exploración de patrones interesantes.
- Analisis de datos a traves del tiempo.

### Modelo de Aprendizaje Automático

Tambien implementa un sistema de recomendación de videojuegos utilizando el enfoque de Item-Item:

- **Ítem-Ítem**: Este sistema recomienda juegos similares a un juego dado.

- Se ha creado la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP, (NLTK)
- La columna 'sentiment_analysis' reemplaza la columna 'user_reviews.review' según lo especificado.

 

### Desarrollo de la API

- Se han creado las siguientes funciones para los endpoints de la API:

+ def **developer( *`desarrollador` : str* )**:
    `Cantidad de items y porcentaje` de contenido Free por año según empresa desarrolladora

+ def **userdata( *`user_id` : str* )**:
    Devuelve la `cantidad` de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items. 

+ def **UserForGenre( *`género` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

+ def **best_developer_year( *`año` : int* )**:
    Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

+ def **developer_reviews_analysis( *`desarrolladora` : str* )**:
    Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.


+ def **recomendacion_juego( `id de producto`  )**:
   Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
<br/>


### Transformaciones 

- Se ha realizado la lectura de los datasets en el formato JSON.
- Se ha realizado una exhaustiva transformacion de datos, limpieza, imputacion de datos faltantes, etc.
- se han exportado como parquet o csv.
- Las columnas y filas innecesarias se han eliminado para optimizar el rendimiento de la API y el entrenamiento del modelo.







## Video de Demostración

Puedes ver una demostración de la API y el modelo de recomendación en funcionamiento en el siguiente enlace: [Enlace al Video](https://www.youtube.com/)

## Repositorio

El código fuente de este proyecto se encuentra en el siguiente repositorio: [Enlace al Repositorio](https://github.com/juan123531/)

## Fuentes de Datos

- Datasets: [Enlace al Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
# PI_ML_FT16
