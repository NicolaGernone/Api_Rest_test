import unittest

from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from api.application.api_service import ApiService
from api.infrastructure.models import Coin
from api.infrastructure.views import *


class ApiViewTest(APITestCase):
    
    unittest.TestCase.maxDiff = None

    def setUp(self) -> None:
        self.api_service = ApiService()
        self.api_view = ApiClientNames(self.api_service)

    def test_get_ok(self) -> None:
        baker.make(Coin, name='Bitcoin')
        response = self.client.get('/coin/names/')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_get_fail(self) -> None:
        baker.make(Coin, name='Ethereum')
        response = self.client.get('/coin/no')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)