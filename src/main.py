import requests
from bs4 import BeautifulSoup
import json


class CinemaXXIScrapper:
    def __init__(self):
        """
        A constructor function.
        """
        self.endPoint = "https://m.21cineplex.com/"

    def getComingSoon(self):
        """
        It gets the coming soon movies from the website.
        :return: A list of dictionaries.
        """
        list_data = []
        request_getComingSoon = requests.get(
            url=self.endPoint + "gui.coming_soon.php"
        )
        soup = BeautifulSoup(request_getComingSoon.text, 'html.parser')
        for data in soup.find_all('div', class_='grid_movie'):
            list_data.append({
                'movieId': data.find_next('a').get('href').split("&")[1].replace("movie_id=", ""),
                'image': data.find_next('img').get('src'),
                'title': data.find_next('div', class_='title').text,
                'movieType': data.find_next('div', class_='btn-group-sm rating').find_next('span',
                                                                                           class_='btn btn-default btn-outline disabled').text,
                'rating': data.find_next('div', class_='btn-group-sm rating').find_next('a',
                                                                                        class_='btn btn-default btn-outline disabled').text
            })
        return json.dumps(
            list_data,
            indent=4
        )

    def getCityId(self):
        """
        It gets the cityId and cityName from the endpoint gui.list_city.php and returns it as a JSON object
        :return: A list of dictionaries containing the cityId and cityName.
        """
        list_data = []
        request_getCityId = requests.get(
            url=self.endPoint + "gui.list_city.php"
        )
        soup = BeautifulSoup(request_getCityId.text, 'html.parser')
        for data in soup.find_all('li', class_='list-group-item'):
            list_data.append({
                'cityId': data.find_next('div').get('onclick').split('=')[3][0:-2],
                'cityName': data.find_next('div').text
            })
        return json.dumps(
            list_data,
            indent=4
        )

    def getTheater(self, city):
        """
        It takes a city ID as an argument, and returns a JSON object containing the name and ID of every cinema in that city

        :param city: The city ID
        :return: a JSON object containing the name of the cinema and the cinema ID.
        """
        list_data_imax = []
        list_data_premiere = []
        list_data_all = []
        request_getTheater = requests.get(
            url=self.endPoint + "gui.list_theater.php?sid=&city_id={city}".format(city=city)
        )
        soup = BeautifulSoup(request_getTheater.text, 'html.parser')
        for data in soup.find_all('div', class_='imax'):
            for data2 in data.find_all('div', id='id'):
                list_data_imax.append({
                    'nameCinema': data2.text,
                    'cinemaId': data2.get('onclick').split("&")[2].replace("cinema_id=", "")
                })
        for data in soup.find_all('div', class_='premiere'):
            for data2 in data.find_all('div', id='id'):
                list_data_premiere.append({
                    'nameCinema': data2.text,
                    'cinemaId': data2.get('onclick').split("&")[2].replace("cinema_id=", "")
                })
        for data in soup.find_all('div', class_='all'):
            for data2 in data.find_all('div', id='id'):
                list_data_all.append({
                    'nameCinema': data2.text,
                    'cinemaId': data2.get('onclick').split("&")[2].replace("cinema_id=", "")
                })
        return json.dumps(
            {
                'imax': {
                    'data': list_data_imax,
                },
                'premiere': {
                    'data': list_data_premiere
                },
                'all': {
                    'data': list_data_all
                }
            },
            indent=4
        )

    def getPlaying(self):
        """
        It gets the list of movies that are currently playing.
        :return: A list of dictionaries containing the movieId, image, title, movieType, and rating of the movies currently
        playing.
        """
        list_data = []
        request_getPlaying = requests.get(
            url=self.endPoint + "index.php"
        )
        soup = BeautifulSoup(request_getPlaying.text, 'html.parser')
        for data in soup.find_all('div', class_='grid_movie'):
            list_data.append({
                'movieId': data.find_next('a').get('href').split("&")[1].replace("movie_id=", ""),
                'image': data.find_next('img').get('src'),
                'title': data.find_next('div', class_='title').text,
                'movieType': data.find_next('div', class_='btn-group-sm rating').find_next('span',
                                                                                           class_='btn btn-default btn-outline disabled').text,
                'rating': data.find_next('div', class_='btn-group-sm rating').find_next('a',
                                                                                        class_='btn btn-default btn-outline disabled').text
            })
        return json.dumps(
            list_data,
            indent=4
        )

    def getMovieDetails(self, movie_id):
        """
        It gets the movie details from the movie id

        :param movie_id: The ID of the movie you want to get the details of
        :return: A JSON object containing the movie name, info, and the movie details.
        """
        request_getMovieDetails = requests.get(
            url=self.endPoint + "gui.movie_details.php?sid=&movie_id={movie_id}".format(movie_id=movie_id)
        )
        soup = BeautifulSoup(request_getMovieDetails.text, 'html.parser')
        data = soup.find('div', class_='col-md-9 col-sm-6 col-xs-6')

        return json.dumps({
            'movieName': soup.find_all('div', class_='col-xs-8 col-sm-11 col-md-11')[0].find_next('div').text,
            'info': {
                'genre': soup.find_all('div', class_='col-xs-8 col-sm-11 col-md-11')[1].find_next('div').text.replace(
                    ", ", ",").split(","),
                'dimensions': data.find_all('p')[1].text.strip(),
                'duration': data.find_all('p')[0].text.strip(),
                'ageRate': soup.find('div', class_='col-xs-3 col-sm-1 col-md-1').find('img').get('src'),
                'image': soup.find('div', class_='col-md-3 col-sm-6 col-xs-6').find('img').get('src'),
                'trailer': data.find_all('p')[4].find_next('button').get('onclick').replace("location.href = '", "")[
                           0:-2],
                'desc': soup.find('p', id='description').text,
                'producer': soup.find_all('p', style='margin-bottom: 5px')[0].find_next('p').text.strip(),
                'director': soup.find_all('p', style='margin-bottom: 5px')[1].find_next('p').text,
                'writer': soup.find_all('p', style='margin-bottom: 5px')[2].find_next('p').text.replace(", ",
                                                                                                        ",").split(","),
                'cast': soup.find_all('p', style='margin-bottom: 5px')[3].find_next('p').text.replace(", ", ",").split(
                    ","),
                'distributor': soup.find_all('p', style='margin-bottom: 5px')[4].find_next('p').text,
            },
        },
            indent=4)

    def getSchedule(self, cinema_id):
        """
        It gets the schedule of a movie in a cinema

        :param cinema_id: The cinema ID
        """
        list_data_final = []
        list_data_collection = []

        request_getSchedule = requests.get(
            url=self.endPoint + "gui.schedule.php?sid=&find_by=1&cinema_id={cinema_id}&movie_id=".format(
                cinema_id=cinema_id)
        )
        soup = BeautifulSoup(request_getSchedule.text, 'html.parser')

        time_data = []
        for a in range(0, len(soup.find_all('p', class_='p_time pull-left'))):
            time_data.append(soup.find_all('p', class_='p_time pull-left')[a].text)

        data_status = []
        for datas in soup.find_all('p', class_='p_time pull-left'):
            for data_ in datas.find_all('a'):
                try:
                    if "disabled" in " ".join(data_['class']):
                        data_status.append(False)
                    else:
                        data_status.append(True)
                except KeyError:
                    break

        for collection in range(0, len(time_data)):
            data_collection = []
            for collectione in range(len(data_status[0: len(time_data[collection].split(" ")[0:-1])])):
                data_collection.append({
                    'time': time_data[collection].split(" ")[0:-1][collectione],
                    'can_booking': data_status[0: len(time_data[collection].split(" ")[0:-1])][collectione]
                })
            list_data_collection.append(data_collection)

        i = 0
        for data in soup.find_all('li', class_='list-group-item'):
            list_data_final.append({
                'movieName': data.find('a').find_next('a').text,
                'image': data.find('a').find_next('img').get('src'),
                'dimensions': data.find_all('span', class_='btn btn-default btn-outline disabled')[0].text,
                'ageRate': data.find_all('span', class_='btn btn-default btn-outline disabled')[1].text,
                'duration': data.find('div', style='margin-top:10px; font-size:12px; color:#999').text.strip(),
                'date': data.find('p', class_='p_date').text,
                'price': data.find('span', class_='p_price').text,

                'schedule': list_data_collection[i]

            })
            i += 1

        return json.dumps(
            {
                'cinemaName': soup.find('h4').find('span').find('strong').text,
                'location': soup.find('a', class_='map-link').get('href'),
                'address': soup.find_all('h4')[1].find_next('span').get_text(separator="<br/>").split("<br/>")[0],
                'contact': '',
                'data': list_data_final,
            },
            indent=4
        )

    def getFoodBeverage(self, cinema_id):
        """
        It takes a cinema_id as an argument, and returns a JSON object containing the food and beverage items available at
        that cinema

        :param cinema_id: The ID of the cinema you want to get the schedule from
        :return: a JSON object containing the data of the food and beverage menu.
        """
        list_data_paket = []
        list_data_bakery = []
        list_data_drinks = []
        list_data_popcorn = []
        list_data_fritters = []
        list_data_lightmeal = []
        list_data_snackcandy = []

        request_getFoodBeverage = requests.get(
            url=self.endPoint + "gui.fnb_product.php?sid=&cinema_id={cinema_id}&movie_id=".format(
                cinema_id=cinema_id)
        )
        soup = BeautifulSoup(request_getFoodBeverage.text, 'html.parser')
        for data in soup.find_all('div', id='Paket'):
            for data_ in data.find_all('li'):
                try:
                    list_data_paket.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass
        for data in soup.find_all('div', id='Popcorn'):
            for data_ in data.find_all('li'):
                try:
                    list_data_popcorn.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass
        for data in soup.find_all('div', id='Fritters'):
            for data_ in data.find_all('li'):
                try:
                    list_data_fritters.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass

        for data in soup.find_all('div', id='LightMeal'):
            for data_ in data.find_all('li'):
                try:
                    list_data_lightmeal.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass
        for data in soup.find_all('div', id='Bakery'):
            for data_ in data.find_all('li'):
                try:
                    list_data_bakery.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass
        for data in soup.find_all('div', id='Snack-Candy'):
            for data_ in data.find_all('li'):
                try:
                    list_data_snackcandy.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass
        for data in soup.find_all('div', id='Drinks'):
            for data_ in data.find_all('li'):
                try:
                    list_data_drinks.append({
                        'name': " ".join(data_.find('div', 'col-sm-7').text.split()),
                        'image': data_.find('a', 'image-link pull-left gap-left').get('href'),
                        'price': data_.find('div', 'col-sm-2').text,

                    })
                except AttributeError:
                    pass

        return json.dumps({
            'cinema': soup.find('span', style='font-weight: bold;').text.split("-")[1].strip(),
            'data_food': {
                'Paket': list_data_paket,
                'Bakery': list_data_bakery,
                'Drinks': list_data_drinks,
                'Popcorn': list_data_popcorn,
                'Fritters': list_data_fritters,
                'Lightmeal': list_data_lightmeal,
                'Snackcandy': list_data_snackcandy
            },

        }, indent=4)
