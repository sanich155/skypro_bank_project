import json
from src.external_api import convert
def get_trans_list(filename: str) -> list:
    """Получает путь до JSON-файла и возвращает список словарей с транзакциями"""


    try:
        with open(filename, 'r', encoding='utf-8') as f:
            trans_list = json.load(f)
            return trans_list

    except:
        return list()


def count_trans_sum(transaction: dict):
    """Получает на вход транзакцию и выводит её сумму в рублях"""

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return transaction['operationAmount']['amount']
    else:
        currency = transaction['operationAmount']['currency']['code']
        amount = transaction['operationAmount']['amount']
        result = convert(amount, currency)
        return result


