from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.schema import response_schema_dict, days_parameter
from api.services import FetchWeatherData


class GetLocationWeatherAPIView(APIView):
    """
    Api view to get the temperature values for user entered
    location.
    """

    @swagger_auto_schema(manual_parameters=[days_parameter], responses=response_schema_dict,
                         operation_id='Get Location Temperature')
    def get(self, *args, **kwargs):
        query_city = kwargs['city']
        query_days = self.request.GET.get('days', None)
        weather_service = FetchWeatherData()
        weather_service.city = query_city
        weather_service.days = query_days
        data = weather_service.get_weather_data()
        if data['status_code'] == 200:
            return Response(data['data'], status=status.HTTP_200_OK)
        else:
            return Response(data['error'], status=status.HTTP_400_BAD_REQUEST)
