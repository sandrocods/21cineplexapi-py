from flask import Flask

from src.main import *

app = Flask(__name__)
cinemaClass = CinemaXXIScrapper()


@app.route("/getComingSoon")
def getComingSoon():
    return cinemaClass.getComingSoon()


@app.route("/getCurrentlyPlaying")
def getCurrentlyPlaying():
    return cinemaClass.getPlaying()


@app.route("/getCityId")
def getCityId():
    return cinemaClass.getCityId()


@app.route("/getTheaters/<cityId>")
def getTheaters(cityId):
    return cinemaClass.getTheater(city=cityId)


@app.route("/getMovies/<movieId>")
def getMovies(movieId):
    return cinemaClass.getMovieDetails(movie_id=movieId)


@app.route("/getSchedule/<cinemaId>")
def getSchedule(cinemaId):
    return cinemaClass.getSchedule(cinema_id=cinemaId)


@app.route("/getFoodsBeverages/<cinemaId>")
def getFoodsBeverage(cinemaId):
    return cinemaClass.getFoodBeverage(cinema_id=cinemaId)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
