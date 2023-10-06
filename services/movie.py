from models.movie import Movie as MovieModel
from schema.movie import Movies
class MovieService():

    def __init__(self,db) -> None:
        self.db = db
    
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movie_category(self, category,year):
        result = self.db.query(MovieModel).filter((MovieModel.category == category) | (MovieModel.year == year)).all()
        return result
    
    def create_movie(self, movie: Movies):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        
    def update_movie(self, id: int, data: Movies):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(movie)
        self.db.commit()
        return  

    

    