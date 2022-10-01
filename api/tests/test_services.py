from unittest import mock

from .test_setup import TestSetup


class TestGetLocationWeatherService(TestSetup):
    @mock.patch('api.services.requests.get')
    def test_class_constructor(self, mock_get):
        """
        Testing the class __init__ method
        """
        self.assertEqual(self.weather_service.city, self.valid_city)
        self.assertEqual(self.weather_service.days, self.days)

    @mock.patch('api.services.requests.get')
    def test_with_valid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.successful_mock
        response = self.weather_service.get_weather_data()

        self.assertEquals(response['status_code'], 200)
        self.assertEquals(response['data'], self.expected_successful_response_dict)
        mock_get.assert_called_once_with(self.api_url)

    @mock.patch('api.services.requests.get')
    def test_with_invalid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.unsuccessful_mock
        response = self.weather_service.get_weather_data()
        self.assertEqual(response, self.unsuccessful_expected_response_dict)
