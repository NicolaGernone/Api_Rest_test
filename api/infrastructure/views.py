from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from api.application.api_service import ApiService


class ApiClientNames(APIView):
    """
    GET Coins Names.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    def get(self, request) -> JsonResponse:
        return JsonResponse(self.service.get_data_names(), status=status.HTTP_200_OK, safe=False)

class ApiClientClose(APIView):
    """
    GET Close value.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    def get(self, request, symbol, date) -> JsonResponse:
        return JsonResponse(self.service.get_close_data(symbol, date), status=status.HTTP_200_OK, safe=False)

class ApiClientMaxProfit(APIView):
    """
    GET maximised profit.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    def get(self, request, symbol, start, end) -> JsonResponse:
        return JsonResponse(self.service.get_maximise_profit_data(symbol, start, end), status=status.HTTP_200_OK, safe=False)
