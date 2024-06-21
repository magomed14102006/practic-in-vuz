import requests

url = 'https://api.binance.com/api/v3/ticker/price'


def price():
    response = requests.get(url, {"symbol": "BTCUSDT"})
    data = response.json()
    data = data["price"]
    return data


print(price())