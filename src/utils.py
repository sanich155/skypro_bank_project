import json
import os

def get_trans_list(filename: str) -> list:
    """Получает путь до JSON-файла и возвращает список словарей с транзакциями"""

    try:
        with open(os.path.abspath(filename), 'r', encoding='utf-8') as f:
            trans_list = json.load(f)
            return trans_list
    except:
        return list()
