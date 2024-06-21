from django.shortcuts import render
import requests

url = 'https://api.binance.com/api/v3/ticker/price'


# def price():
#     response = requests.get(url, {"symbol": "BTCUSDT"})
#     data = response.json()
#     data = data["price"]
#     return data
#
#
# result = price()

def index(request):
    api_url = url
    response = requests.get(api_url, {"symbol": "BTCUSDT"})
    if response.status_code == 200:
        data = response.json()
        data = data["price"]
    else:
        data = {}
    return render(request, 'main/index.html', {'data': data})


# def index(request):
#     return render(request, 'main/index.html', {'data': result})


def about(request):
    return render(request, 'main/about.html')
