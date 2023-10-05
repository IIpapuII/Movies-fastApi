from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from middleware.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.auth import auth_router

app = FastAPI()
app.title = "Peliculas Fast-Api"
app.version = "1.2"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=["Home"])
def message():
    return HTMLResponse('<h1> Hellor Wordl </h1>')



