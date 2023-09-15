from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse



movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2010',
        'rating': 7.8,
        'category': 'anime'    
    },
        {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'comedia'    
    },   {
        'id': 3,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2011',
        'rating': 7.8,
        'category': 'accion'    
    } 
]

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
def create_movie():
    pass