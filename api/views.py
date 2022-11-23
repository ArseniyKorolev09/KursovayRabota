from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Predictions
from .seriaalizers import Predictions_Serializers
from func_app.predictions import create_predict_valuta_plot


# Create your views here.

class predictions_Views(APIView):

    def get(self, request, days_num):
        if days_num <= 15:
            predictions_currency = Predictions("ok", create_predict_valuta_plot(days_num))
        else:
            predictions_currency = Predictions("error", "Too many days")
        serializers_for_request = Predictions_Serializers(instance=predictions_currency)
        return Response(serializers_for_request.data)
