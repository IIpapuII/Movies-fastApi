from fastapi import FastAPI,Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from controller.jsonRead import movies, save_json_data
from schema.movie import Movies, User
from controller.jwt_manager import create_token

app = FastAPI()
app.title = "Peliculas Fast-Api"
app.version = "1.2"


@app.get('/', tags=["Home"])
def message():
    return HTMLResponse('<h1> Hellor Wordl </h1>')

@app.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return token

@app.get('/movies', tags=['movies'] ,response_model= Movies, status_code= 200)
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id:int = Path(ge=1, le=2000)):
    for item in movies:
        if item["id"] == id :
            return item
    return []

@app.get('/movies/', tags=['movies'], response_model=Movies)
def get_movies_by_querys_category(category: str = Query(min_length=5, max_length=15), year:int = Query(le=2022)) -> list:
    for item in movies:
        if item["category"] == category or int(item["year"])==year:
            return item
    return JSONResponse(status_code=404, content=[])

@app.post('/movies',tags=['movies'], response_model= dict, status_code=201)
def create_movie(movie: Movies):
    movies.append(movie.dict())
    save_json_data(movies)
    return "Save Data "

@app.put('/movies/{movie_id}', tags=['movies'])
def update_movie(movie_id: int, movie: Movies):
    for item in movies:
        if item["id"] == movie_id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
    save_json_data(movies)
    return "Update Movie "

@app.delete('/movies/{movie_id}', tags=['movies'])
def delete_movie(movie_id: int):
    for i in movies:
        if i["id"] == movie_id:
            movies.remove(i)
    save_json_data(movies)
    return f'Delete movie {movie_id}'