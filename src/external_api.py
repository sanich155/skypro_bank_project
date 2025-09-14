import requests

def convert(amount: float, currency: str) -> float:
    """Конвертирует в рубль через https://apilayer.com/marketplace/exchangerates_data-api"""

    url = 'https://api.apilayer.com/exchangerates_data/convert'
    headers = {'apikey': 'U2Ecesy02WFFQxrpLIWNFKoTe3o4EltH'}
    parameters = {'amount': amount, 'from': currency, 'to': 'RUB'}
    response = requests.get(url, headers=headers, params=parameters)

    return round(response.json()['result'], 2)


