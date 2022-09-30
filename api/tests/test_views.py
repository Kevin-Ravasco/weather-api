from django.urls import reverse

from .test_setup import TestSetup


class TestGetLocationWeatherAPIView(TestSetup):

    def test_with_valid_location(self):
        city = 'Nairobi'
        url = reverse('location_weather', kwargs={'city': city})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('maximum' in response.data)
        self.assertTrue('minimum' in response.data)
        self.assertTrue('average' in response.data)
        self.assertTrue('median' in response.data)

    def test_with_invalid_location(self):
        city = 'Nairobix'  # note the x after Nairobi
        url = reverse('location_weather', kwargs={'city': city})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 400)
