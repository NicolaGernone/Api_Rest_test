from api.infrastructure.models import Coin
from django.http import Http404
from rest_framework.request import HttpRequest

from .domain.utilities.days_calculator import days_range
from .domain.utilities.max_profit_algrt import max_profit


class ApiService:
    
    def get_data_names(self, name: str):
        """Retrive the names of the coins in the DB with the id
        """
        try:
            names = Coin.objects.only('name').distinct('name')
            return { 'Coins Names' : names }
        except Data.DoesNotExist as e:
            raise Http404(e)
    
    def get_close_data(self, symbol: str, date: str):
        """Select the close value per coin in a selected date
        """
        try:
            data = Coin.objects.filter(symbol=symbol).filter(date=date)
            return {'Coin' : symbol, 'Date' : date, 'Close' : data.close }
        except Data.DoesNotExist as e:
                raise Http404(e)
    

    def get_maximise_profit_data(self, start: str, end: str):
        """Calculate and return the Maximised Profit for a given range of dates
        """
        try:
            days = days_range(start, end)
            prices = Coin.objects.filter(created_at__gte=start, created_at__lte=end)
            mx_profit = max_profit(prices, days)
            return { 'Start Date': start, 'End Date': end, 'Max Profit': mx_profit }
        except Data.DoesNotExist as e:
            raise Http404(e)
