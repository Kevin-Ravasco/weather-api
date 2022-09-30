from django.test import SimpleTestCase
from django.urls import reverse, resolve

from api.views import GetLocationWeatherAPIView


class TestUrls(SimpleTestCase):
    def test_signup_url(self):
        city = 'Nairobi'
        url = reverse('location_weather', kwargs={'city': city})
        resolved = resolve(url)
        self.assertEqual(resolved.func.__name__, GetLocationWeatherAPIView.as_view().__name__)
        self.assertEqual(url, f"/api/locations/{city}/")
