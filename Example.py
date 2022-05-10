from src.main import *

cinemaClass = CinemaXXIScrapper()
print(
    cinemaClass.getSchedule(cinema_id='JKTARGA')
)

print(
    cinemaClass.getFoodBeverage(cinema_id='JKTARGA')
)


print(
    cinemaClass.getPlaying()
)


print(
    cinemaClass.getCityId()
)

print(
    cinemaClass.getTheater(city=29)
)

print(
    cinemaClass.getComingSoon()
)

print(
    cinemaClass.getMovieDetails(movie_id='22DSX2')
)

