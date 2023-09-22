from fastapi import FastAPI, Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from schema.movie import Movies, User, JWTBearer
from controller.jwt_manager import create_token
from typing import List
from config.database import Base, engine, session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middleware.error_handler import ErrorHandler
from middleware.jwt_bearer import JWTBearer

app = FastAPI()
app.title = "Peliculas Fast-Api"
app.version = "1.2"
app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=["Home"])
def message():
    return HTMLResponse('<h1> Hellor Wordl </h1>')

@app.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return token

@app.get('/movies', tags=['movies'] ,response_model= Movies, status_code= 200, dependencies= [Depends(JWTBearer())])
def get_movies()-> List[Movies]:
    db = session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200,content= jsonable_encoder(result))

@app.get('/movies/{id}', tags=['movies'], response_model=List[Movies], status_code=200,)
def get_movie(id:int = Path(ge=1, le=2000)):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code= 404, content= {'message':"Pelicula no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/movies/', tags=['movies'], response_model=Movies)
def get_movies_by_querys_category(category: str = Query(min_length=5, max_length=15), year:int = Query(le=2022)) -> list:
    db = session()
    result = db.query(MovieModel).filter((MovieModel.category == category) | (MovieModel.year == year)).all()

    if not result:
        return JSONResponse(status_code= 404, content= {'menssage':"No se encontro la pelicula"})
    return JSONResponse(status_code=404, content= jsonable_encoder(result))

@app.post('/movies',tags=['movies'], response_model= dict, status_code=201)
def create_movie(movie: Movies):
    db = session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

@app.put('/movies/{movie_id}', tags=['movies'])
def update_movie(movie_id: int, movie: Movies):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message": "Se ha registrado la pelicula"})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code=200, content={'menssage': "Pelicula actualizada"})

@app.delete('/movies/{movie_id}', tags=['movies'])
def delete_movie(movie_id: int):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message": "Se ha registrado la pelicula"})
    db.delete(result)
    db.commit()
    return f'Delete movie {movie_id}' 