
# 21cineplex API

Scraping data dari 21cineplex untuk keperluan pembelajaran dan riset, tidak ada hal yang berbahaya atau dapat merugikan website sumber.


## Build With

 - [Python3](https://www.python.org/)
 - [Requests](https://pypi.org/project/requests/)
 - [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 - [Json](https://docs.python.org/3.10/library/json.html)
 - [Flask](https://pypi.org/project/Flask/)


## Installation

Git Clone this project

```bash
  cd 21cineplexapi-py
  pip install .\requirements.txt
```


## Usage / Examples

use Example.py

```python
    from src.main import *

    cinemaClass = CinemaXXIScrapper()
    # Gets the list of movies that are currently playing.
    print(
        cinemaClass.getPlaying()
    )
```
Output
```bash
    [
        {
            "movieId": "22DSMM",
            "image": "https://web3.21cineplex.com/movie-images/22DSMM.jpg",
            "title": "DOCTOR STRANGE IN THE MULTIVERSE OF MADNESS",
            "movieType": "2D",
            "rating": "R13+"
        },
        {
            "movieId": "22DSX2",
            "image": "https://web3.21cineplex.com/movie-images/22DSX2.jpg",
            "title": "DOCTOR STRANGE IN THE MULTIVERSE OF MADNESS (IMAX 2D)",
            "movieType": "IMAX 2D",
            "rating": "R13+"
        },
        {
            "movieId": "10KDDP",
            "image": "https://web3.21cineplex.com/movie-images/10KDDP.jpg",
            "title": "KKN DI DESA PENARI",
            "movieType": "2D",
            "rating": "D17+"
        },

```
    
## API Reference

### Gets the list of movies that are currently playing

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getPlaying()
    )
```
#### Output
![App Screenshot](https://i.ibb.co/dkb29yt/image.png)

### Gets the coming soon movies

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getComingSoon()
    )

```
#### Output
![App Screenshot](https://i.ibb.co/X7JkM4D/image.png)

### Gets the cityId and cityName

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getCityId()
    )
```
#### Output
![App Screenshot](https://i.ibb.co/WFtS9XH/image.png)

### Gets the nameCinema and cinemaID in that city

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getTheater(city=)
    )
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `city` | `integer` | **Required**. cityId  |

#### Output
![App Screenshot](https://i.ibb.co/RCf5TYf/image.png)

### Gets the movie details from the movie id

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getMovieDetails(movie_id='')
    )

```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `movie_id` | `string` | **Required**. movie_id  |

#### Output
![App Screenshot](https://i.ibb.co/kK5RV2d/image.png)

### Gets food and beverage items available at that cinema

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getFoodBeverage(cinema_id='')
    )

```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `cinema_id` | `string` | **Required**. cinema_id  |

#### Output
![App Screenshot](https://i.ibb.co/2nXGB62/image.png)


### Gets the schedule of a movie in a cinema

```python
    cinemaClass = CinemaXXIScrapper()
    print(
        cinemaClass.getSchedule(cinema_id='')
    )

```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `cinema_id` | `string` | **Required**. cinema_id  |

#### Output
![App Screenshot](https://i.ibb.co/qnM2jcm/image.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/sandrocods/21cineplexapi-py/
```

Go to the project directory

```bash
  cd 21cineplexapi-py
```

Install dependencies

```bash
   pip install .\requirements.txt
```

Start the Flask server

```bash
  python3 index.py
```


## Flask API Reference

### Gets the list of movies that are currently playing

```http
    GET /getCurrentlyPlaying
```

### Gets the coming soon movies

```http
    GET /getComingSoon
```

### Gets the cityId and cityName

```http
    GET /getCityId
```

### Gets the nameCinema and cinemaID in that city

```http
    GET /getTheaters/<cityId>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `cityId` | `integer` | **Required**. cityId  |


### Gets the movie details from the movie id

```http
    GET /getMovies/<movieId>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `movieId` | `string` | **Required**. movieId  |


### Gets food and beverage items available at that cinema

```http
    GET /getFoodsBeverages/<cinemaId>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `cinemaId` | `string` | **Required**. cinemaId  |


### Gets the schedule of a movie in a cinema

```http
    GET /getSchedule/<cinemaId>
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `cinemaId` | `string` | **Required**. cinemaId  |

## Authors

- [@sandrocods](https://www.github.com/sandrocods)

