import statistics

import requests
from django.conf import settings


class FetchWeatherData:
    """
    To handle the fetching of weather data from the external api
    """
    def __int__(self, city: str, days: int = 1) -> None:
        self.api_key = settings.WEATHER_API_KEY
        self.city = city
        self.days = days

    def fetch_api_weather_data(self) -> tuple[int, dict]:
        """
        Makes the api call to the external weather api and returns
        the response.
        """
        url = f"http://api.weatherapi.com/v1/forecast.json?key={settings.WEATHER_API_KEY}" \
              f"&q={self.city}&days={self.days}"

        r = requests.get(url)
        response_status_code = r.status_code
        data = r.json()
        return response_status_code, data

    def clean_temperature(self, data_list: list) -> dict:
        """
        To return a list of temperatures fetched (max and min) and average data
        """
        max_min_list = []
        average = []
        for item in data_list:
            temp_dict = item['day']
            max_min_list.append(temp_dict['maxtemp_c'])
            max_min_list.append(temp_dict['mintemp_c'])
            average.append(temp_dict['avgtemp_c'])

        data = {
            'max_min_list': max_min_list,
            'average': average
        }
        return data

    def compute_temperature(self, data: dict) -> dict:
        """
        To compute the maximum, minimum, average and median temperatures
        from the input data.
        """
        max_min_list = data['max_min_list']
        average = data['average']

        data = {
            'maximum': max(max_min_list),
            'minimum': min(max_min_list),
            'average': statistics.mean(average),
            'median': statistics.median(max_min_list)
        }
        return data

    def get_weather_data(self) -> dict:
        status_code, response_data = self.fetch_api_weather_data()
        data = {'status_code': status_code}
        if status_code == 200:
            cleaned_data = self.clean_temperature(response_data['forecast']['forecastday'])
            computed_temperatures = self.compute_temperature(cleaned_data)
            data['data'] = computed_temperatures
        else:
            data['message'] = response_data['error']['message']
        return data
