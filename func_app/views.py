from django.http import HttpResponse
from django.shortcuts import render
from func_app.predictions import create_predict_valuta_plot


def give_predictions(request, days_num):
    if days_num <= 15:
        context = {
            'days_num': days_num,
            'filename': create_predict_valuta_plot(days_num)
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponse("error: to many days no over 15")
