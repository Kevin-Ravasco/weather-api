from rest_framework.test import APITestCase

from django.test import Client


class TestSetup(APITestCase):
    """
    Base setup for our test cases
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        return
