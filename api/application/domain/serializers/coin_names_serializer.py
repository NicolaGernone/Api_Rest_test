from rest_framework import serializers

from api.infrastructure.models import Coin


class CoinNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ['name']