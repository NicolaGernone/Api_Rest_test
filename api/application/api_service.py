import datetime

from django.http import Http404

from api.application.domain.serializers.coin_close_serializer import \
    CoinCloseSerializer
from api.application.domain.serializers.coin_names_serializer import \
    CoinNamesSerializer
from api.infrastructure.models import Coin

from .domain.utilities.days_calculator import days_range
from .domain.utilities.max_profit_algrt import stockBuySell


class ApiService:
    
    def get_data_names(self):
        """Retrive the names of the coins in the DB with the id
        """
        try:
            names = Coin.objects.distinct('name')
            serializer = CoinNamesSerializer(names, many=True)
            return serializer.data
        except Coin.DoesNotExist as e:
            raise Http404(e)
    
    def get_close_data(self, symbol: str, date: str):
        """Select the close value per coin in a selected date"""
        partial_time = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        try:
            data = Coin.objects.filter(symbol=symbol).filter(date__date=partial_time)
            serializer = CoinCloseSerializer(data, many=True)
            return serializer.data
        except Coin.DoesNotExist as e:
                raise Http404(e)
    

    def get_maximise_profit_data(self, symbol: str, start: str, end: str):
        """Calculate and return the Maximised Profit for a given range of dates
        """
        try:
            partial_start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
            partial_end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
            days = days_range(partial_start, partial_end)
            data = Coin.objects.filter(symbol=symbol).filter(date__range=[partial_start, partial_end])
            print(days)
            print(data.values_list('close', flat=True))
            prices = data.values_list('close', flat=True)
            return stockBuySell(prices, days)
        except Coin.DoesNotExist as e:
            raise Http404(e)
