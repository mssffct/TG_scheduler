from django.http import JsonResponse
from rest_framework.response import Response


class SuccessResponse:
    def __new__(cls, data=None, json_response=False, *args, **kwargs):
        data = {} if data is None else data

        response_model = JsonResponse if json_response else Response

        return response_model(data, status=200)


class ErrorResponse:
    def __new__(cls, description: str = None, json_response=False, status: int = 503, **kwargs):
        data = {'description': description} | kwargs

        response_model = JsonResponse if json_response else Response

        return response_model(data, status=status)