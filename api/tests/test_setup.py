from unittest import mock

from django.conf import settings
from rest_framework.test import APITestCase

from django.test import Client

from api.services import FetchWeatherData


class TestSetup(APITestCase):
    """
    Base setup for our test cases
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.valid_city = 'Nairobi'
        cls.invalid_city = 'Nairobix'  # note the x after Nairobi
        cls.days = 2
        cls.api_url = f"http://api.weatherapi.com/v1/forecast.json?key={settings.WEATHER_API_KEY}" \
                      f"&q={cls.valid_city}&days={cls.days}"

        # set up successful mock request
        # this is the json received for city Nairobi, for 2 days in
        # an actual api call we use it as our expected dict
        external_api_response_dict = {
            "location": {
                "name": "Nairobi",
                "region": "Nairobi Area",
                "country": "Kenya",
                "lat": -1.28,
                "lon": 36.82,
                "tz_id": "Africa/Nairobi",
                "localtime_epoch": 1664527179,
                "localtime": "2022-09-30 11:39"
            },
            "current": {
                "last_updated_epoch": 1664526600,
                "last_updated": "2022-09-30 11:30",
                "temp_c": 20.0,
                "temp_f": 68.0,
                "is_day": 1,
                "condition": {
                    "text": "Partly cloudy",
                    "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                    "code": 1003
                },
                "wind_mph": 5.6,
                "wind_kph": 9.0,
                "wind_degree": 360,
                "wind_dir": "N",
                "pressure_mb": 1023.0,
                "pressure_in": 30.21,
                "precip_mm": 0.0,
                "precip_in": 0.0,
                "humidity": 60,
                "cloud": 75,
                "feelslike_c": 20.0,
                "feelslike_f": 68.0,
                "vis_km": 10.0,
                "vis_miles": 6.0,
                "uv": 5.0,
                "gust_mph": 6.7,
                "gust_kph": 10.8
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2022-09-30",
                        "date_epoch": 1664496000,
                        "day": {
                            "maxtemp_c": 29.7,
                            "maxtemp_f": 85.5,
                            "mintemp_c": 15.0,
                            "mintemp_f": 59.0,
                            "avgtemp_c": 20.4,
                            "avgtemp_f": 68.7,
                            "maxwind_mph": 14.5,
                            "maxwind_kph": 23.4,
                            "totalprecip_mm": 0.2,
                            "totalprecip_in": 0.01,
                            "avgvis_km": 10.0,
                            "avgvis_miles": 6.0,
                            "avghumidity": 59.0,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": 86,
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": 0,
                            "condition": {
                                "text": "Patchy rain possible",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                                "code": 1063
                            },
                            "uv": 5.0
                        },
                    },
                    {
                        "date": "2022-10-01",
                        "date_epoch": 1664582400,
                        "day": {
                            "maxtemp_c": 30.4,
                            "maxtemp_f": 86.7,
                            "mintemp_c": 14.1,
                            "mintemp_f": 57.4,
                            "avgtemp_c": 20.4,
                            "avgtemp_f": 68.6,
                            "maxwind_mph": 14.1,
                            "maxwind_kph": 22.7,
                            "totalprecip_mm": 0.5,
                            "totalprecip_in": 0.02,
                            "avgvis_km": 9.8,
                            "avgvis_miles": 6.0,
                            "avghumidity": 60.0,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": 80,
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": 0,
                            "condition": {
                                "text": "Patchy rain possible",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                                "code": 1063
                            },
                            "uv": 5.0
                        },
                    }
                ]
            }
        }
        cls.successful_mock = mock.Mock()
        cls.successful_mock.json.return_value = external_api_response_dict
        cls.successful_mock.status_code = 200

        # our expected response after being computed should be this
        # with response value from external api being the expected_dict
        cls.expected_successful_response_dict = {
            "maximum": 30.4,
            "minimum": 14.1,
            "average": 20.4,
            "median": 22.35
        }

        # set up unsuccessful mock
        cls.unsuccessful_mock = mock.Mock()
        cls.unsuccessful_expected_response_dict = {'error': {'message': 'Invalid city name'}, 'status_code': 400}
        cls.unsuccessful_mock.json.return_value = cls.unsuccessful_expected_dict
        cls.unsuccessful_mock.status_code = 400

        cls.weather_service = FetchWeatherData(cls.valid_city, cls.days)
        return
