from django.urls import path

from api.views import GetLocationWeatherAPIView

urlpatterns = [
    path('locations/<str:city>/', GetLocationWeatherAPIView.as_view(),
         name='location_weather')
]
