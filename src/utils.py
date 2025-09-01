import json
def get_trans_list(filename: str) -> list:
    """Получает путь до JSON-файла и возвращает список словарей с транзакциями"""
    with open(filename, 'r') as f:
        trans_list = json.load(f)
        return trans_list



def count_trans_sum(transaction: dict):
    """Получает на вход транзакцию и выводит её сумму в рублях"""

    pass
