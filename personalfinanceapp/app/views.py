from django.shortcuts import render
from rest_framework import viewsets

from .models import Portfolio
from .serializers import PortfolioSerializer

# Create your views here.


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    # overwrite default get behaviour
    def get_queryset(self):
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            return self.queryset.filter(user__id=user_id).prefetch_related(
                "instrument_set"
            )
        return self.queryset.none()
