from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import  JSONResponse
from schema.movie import Movies
from typing import List
from config.database import session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middleware.jwt_bearer import JWTBearer
from services.movie import MovieService

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'] ,response_model= Movies, status_code= 200, dependencies= [Depends(JWTBearer())])
def get_movies()-> List[Movies]:
    db = session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content= jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=List[Movies], status_code=200,)
def get_movie(id:int = Path(ge=1, le=2000)):
    db = session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code= 404, content= {'message':"Pelicula no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], response_model=Movies)
def get_movies_by_querys_category(category: str = Query(min_length=5, max_length=15), year:int = Query(le=2022)) -> list:
    db = session()
    result = MovieService(db).get_movie_category(category,year)

    if not result:
        return JSONResponse(status_code= 404, content= {'menssage':"No se encontro la pelicula"})
    return JSONResponse(status_code=404, content= jsonable_encoder(result))

@movie_router.post('/movies',tags=['movies'], response_model= dict, status_code=201)
def create_movie(movie: Movies):
    db = session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

@movie_router.put('/movies/{movie_id}', tags=['movies'])
def update_movie(movie_id: int, movie: Movies):
    db = session()
    result = MovieService(db).get_movie(movie_id)
    if not result:
        return JSONResponse(status_code=404,content={"message": "Se ha registrado la pelicula"})
    MovieService(db).update_movie(movie_id,movie)
    return JSONResponse(status_code=200, content={'menssage': "Pelicula actualizada"})

@movie_router.delete('/movies/{movie_id}', tags=['movies'])
def delete_movie(movie_id: int):
    db = session()
    result = get_movie(movie_id)
    if not result:
        return JSONResponse(status_code=404,content={"message": "Se ha registrado la pelicula"})
    MovieService(db).delete_movie(movie_id)
    return f'Delete movie {movie_id}' 