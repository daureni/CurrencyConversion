from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Currency

import requests
import json

class IndexView(generic.ListView):
    template_name = 'rates/index.html'
    context_object_name = 'current_currency_list'

    def get_queryset(self):
        return Currency.objects.all()


def detail(request, currency_id):
    currency = get_object_or_404(Currency, pk=currency_id)
    response = requests.get('https://openexchangerates.org/api/latest.json?app_id=0853b0c6993a40f7ac040264ca5fb748')
    js = response.json()
    rates = js['rates']
    data = json.loads(json.dumps(rates))
    cur_in_usd = 1 / data[currency.code]
    res = []
    for i in rates:
        res.append({'cur' : i, 'value' : round(cur_in_usd * rates[i],2)})

    return render(request, 'rates/detail.html', {'currency': currency, 'rates_list': res})


