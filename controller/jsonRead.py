import json
movies:list
with open("D:/Project_code/Api-Curso/date.json","r") as Getmovies:
    movies = json.load(Getmovies)

def save_json_data(dateNew):
    with open("D:/Project_code/Api-Curso/date.json","w") as newMovies:
        json.dump(dateNew, newMovies, indent= 4, )