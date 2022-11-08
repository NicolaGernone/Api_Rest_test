from api.application.api_service import ApiService
from rest_framework import status
from rest_framework.response import JsonResponse
from rest_framework.views import APIView


class ApiClient(APIView):
    """
    Retrieve, update or delete istances.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    def get_names(self, request, name) -> JsonResponse:
        return JsonResponse(self.service.get_data_names(name), status=status.HTTP_200_OK)

    def get_close_price(self, request, symbol, date) -> JsonResponse:
        return JsonResponse(self.service.get_close_data(symbol, date), status=status.HTTP_200_OK)

    def get_maximise_profit(self, request, start, end) -> JsonResponse:
        return JsonResponse(self.service.get_maximise_profit_data(start, end), status=status.HTTP_204_NO_CONTENT)
