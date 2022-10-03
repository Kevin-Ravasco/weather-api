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
    def test_fetch_api_weather_data_method(self, mock_get):
        response = self.weather_service.fetch_api_weather_data()
        self.assertEqual(type(response), tuple)

    def test_clean_temperature_method(self):
        input_data = self.external_api_response_dict['forecast']['forecastday']
        data = self.weather_service.clean_temperature(input_data)
        self.assertEqual(type(data), dict)
        self.assertTrue('max_min_list' in data)
        self.assertTrue('average' in data)

    def test_compute_temperature_method(self):
        data = {
            'max_min_list': [1, 2, 3, 4, 5],
            'average': [1.5, 2.5, 3.5, 4.5, 5.5]
        }
        expected_dict = {
            'maximum': 5,
            'minimum': 1,
            'average': 3.5,  # statistics.mean(data['average']) = 3.5
            'median': 3  # statistics.mean(data['max_min_list']) = 3
        }
        computed = self.weather_service.compute_temperature(data)
        self.assertEqual(computed, expected_dict)

    @mock.patch('api.services.requests.get')
    def test_get_weather_data_method_with_valid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.successful_mock
        response = self.weather_service.get_weather_data()

        self.assertEquals(response['status_code'], 200)
        self.assertEquals(response['data'], self.expected_successful_response_dict)
        mock_get.assert_called_once_with(self.api_url)

    @mock.patch('api.services.requests.get')
    def test_get_weather_data_method_with_invalid_location(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.unsuccessful_mock
        response = self.weather_service.get_weather_data()
        self.assertEqual(response, self.unsuccessful_expected_response_dict)
