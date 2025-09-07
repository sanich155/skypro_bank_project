import json
import os
def get_trans_list(filename: str) -> list:
    """Получает путь до JSON-файла и возвращает список словарей с транзакциями"""


    try:
        with open(filename, 'r', encoding='utf-8') as f:
            trans_list = json.load(f)
            return trans_list

    except:
        return list()


print(get_trans_list(os.path.abspath("../data/operations.json")))
print(type(get_trans_list(os.path.abspath("../data/operations.json"))))

def count_trans_sum(transaction: dict):
    """Получает на вход транзакцию и выводит её сумму в рублях"""

    pass

#print(os.path.abspath("../data/operations.json"))