from unittest import mock

from django.urls import reverse

from .test_setup import TestSetup


class TestGetLocationWeatherAPIView(TestSetup):

    @mock.patch('api.services.requests.get')
    def test_with_valid_location_kwargs(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.successful_mock
        url = reverse('location_weather', kwargs={'city': self.valid_city})
        response = self.client.get(url, {'days': self.days})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, self.expected_successful_response_dict)

    @mock.patch('api.services.requests.get')
    def test_with_invalid_location_kwargs(self, mock_get):
        # Define response for the fake API
        mock_get.return_value = self.unsuccessful_mock
        url = reverse('location_weather', kwargs={'city': self.invalid_city})
        response = self.client.get(url, {'days': self.days})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.unsuccessful_expected_response_dict['error'])
