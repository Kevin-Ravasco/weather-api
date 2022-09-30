from unittest import mock

from .test_setup import TestSetup
from ..services import FetchWeatherData


class TestGetLocationWeatherAPIView(TestSetup):

    def setUp(self) -> None:
        self.weather_service = FetchWeatherData()
        self.weather_service.city = self.valid_city
        self.weather_service.days = self.days

    @mock.patch('api.services.requests.get')
    def test_with_valid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.successful_mock

        # making a call to our endpoint
        # response = self.client.get(url, {'days': days})

        response = self.weather_service.get_weather_data()

        # our expected response after being computed should be this
        # with response value from external api being the expected_dict
        expected_response = {
            "maximum": 30.4,
            "minimum": 14.1,
            "average": 20.4,
            "median": 22.35
        }
        self.assertEquals(response['status_code'], 200)
        self.assertEquals(response['data'], expected_response)
        mock_get.assert_called_once_with(self.api_url)

    @mock.patch('api.services.requests.get')
    def test_with_invalid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.unsuccessful_mock
        response = self.weather_service.get_weather_data()
        self.assertEqual(response, self.unsuccessful_expected_dict)
