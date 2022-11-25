from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Predictions
from .seriaalizers import Predictions_Serializers
from func_app.predictions import create_predict_valuta_plot
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Create your views here.

class predictions_Views(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="days_num",
                description="the number of days we are analyzing",
                required=True,
                type=OpenApiTypes.INT
            ),
            OpenApiParameter(
                name="api_key",
                description="API key for authentication",
                required=True,
                type=OpenApiTypes.STR
            )
        ],
        description="Prediction of the exchange rate of the Belarus ruble to the Russian ruble",
        responses={
            200: Predictions_Serializers
        },
        methods=["GET"]
    )
    def get(self, request):
        days_num = int(request.GET.get('days_num'))
        if days_num <= 15:
            predictions_currency = Predictions("ok", create_predict_valuta_plot(days_num))
        else:
            predictions_currency = Predictions("error", "Too many days")
        serializers_for_request = Predictions_Serializers(instance=predictions_currency)
        return Response(serializers_for_request.data)
