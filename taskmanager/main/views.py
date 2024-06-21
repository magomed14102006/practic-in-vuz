from django.shortcuts import render
import requests

url = 'https://api.binance.com/api/v3/ticker/price'


def price():
    response = requests.get(url, {"symbol": "BTCUSDT"})
    data = response.json()
    data = data["price"]
    return data


result = price()


def index(request):
    return render(request, 'main/index.html', {'data': result})


def about(request):
    return render(request, 'main/about.html')
