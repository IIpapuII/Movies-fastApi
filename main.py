from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
from controller.jsonRead import movies, save_json_data
from schema.movie import Movies


app = FastAPI()
app.title = "Peliculas Fast-Api"
app.version = "1.2"
@app.get('/', tags=["Home"])
def message():
    return HTMLResponse('<h1> Hellor Wordl </h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id:int):
    for item in movies:
        if item["id"] == id :
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_querys_category(category: str, year:int ):
    for item in movies:
        if item["category"] == category or int(item["year"])==year:
            return item
    return []

@app.post('/movies',tags=['movies'])
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