from django.http import Http404
from django.test import TestCase
from model_bakery import baker
from rest_framework.request import HttpRequest

from api.application.api_service import ApiService
from api.application.domain.serializers.coin_close_serializer import \
    CoinCloseSerializer
from api.application.domain.serializers.coin_names_serializer import \
    CoinNamesSerializer
from api.infrastructure.models import Coin


class ApiServiceTest(TestCase):

    def setUp(self):
        self.api_service = ApiService()
        self.request = HttpRequest()

    def get_data_names_ok(self):
        name = baker.make(Coin, _quantity=5)
        response = self.api_service.get_data_names()
        dataSet = CoinNamesSerializer(name, many=True)
        self.assertEqual( response, dataSet.data)

    def get_data_names_fail(self):
        baker.make(Coin, _quantity=5)
        with self.assertRaises(Http404):
            self.api_service.get_data_names()

    def get_close_data_ok(self):
        close = baker.make(Coin, _quantity=5)
        response = self.api_service.get_close_data('BTC', '2013-08-09')
        dataSet = CoinCloseSerializer(close, many=True)
        self.assertEqual( response, dataSet.data)

    def get_close_data_fail(self):
        baker.make(Coin, _quantity=5)
        with self.assertRaises(Http404):
            self.api_service.get_close_data()

    def get_maximise_profit_data_ok(self):
        baker.make(Coin, _quantity=5)
        response = self.api_service.get_maximise_profit_data('BTC', '2013-04-29', '2015-8-30')
        self.assertEqual( response, { "Buy Day": 4, "Sell Day": 6 })

    def get_maximise_profit_data_fail(self):
        baker.make(Coin, _quantity=5)
        with self.assertRaises(Http404):
            self.api_service.get_maximise_profit_data()