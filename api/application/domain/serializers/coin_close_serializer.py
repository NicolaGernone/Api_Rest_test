from rest_framework import serializers

from api.infrastructure.models import Coin


class CoinCloseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ['symbol', 'date', 'close']