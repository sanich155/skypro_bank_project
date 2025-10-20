import requests
from dotenv import load_dotenv
import os


def convert(transaction: dict) -> float:
    """Получает на вход транзакцию и выводит её сумму в рублях. Конвертирует через https://apilayer.com/marketplace/exchangerates_data-api"""

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return transaction['operationAmount']['amount']
    else:
        load_dotenv()
        convert_token = os.getenv('API_KEY_CONVERT')
        currency = transaction['operationAmount']['currency']['code']
        amount = transaction['operationAmount']['amount']
        url = 'https://api.apilayer.com/exchangerates_data/convert'
        headers = {'apikey': f'{convert_token}'}
        parameters = {'amount': amount, 'from': currency, 'to': 'RUB'}
        response = requests.get(url, headers=headers, params=parameters)
        return round(response.json()['result'], 2)
