from rest_framework import serializers

from .models import Instrument, Portfolio


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = [
            "id",
            "portfolio",
            "investment_type",
            "institution",
            "ticker_symbol",
            "name",
            "position",
            "market_value",
        ]


class PortfolioSerializer(serializers.ModelSerializer):
    # use the instrumentSerializer to serialize instruments
    # also its flagged as one-to-many
    instruments = InstrumentSerializer(
        many=True, read_only=True, source="instrument_set"
    )

    class Meta:
        model = Portfolio
        fields = ["id", "user", "name", "description", "created_at", "instruments"]
