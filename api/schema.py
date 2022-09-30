from drf_yasg import openapi
from rest_framework import status

# have the days query parameter in the swagger documentation
days_parameter = openapi.Parameter('days', openapi.IN_QUERY,
                                   description="Number of days",
                                   type=openapi.TYPE_NUMBER)

# defining our responses schema
response_schema_dict = {
    status.HTTP_200_OK: openapi.Response(
        description="successful request",
        examples={
            "application/json": {
                "maximum": 29.7,
                "minimum": 13.6,
                "average": 20.1,
                "median": 21.65
            }
        }
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Response(
        description="Bad request parameters",
        examples={
            "application/json": {
                "message": 'Invalid city name'
            }
        }
    ),
}
