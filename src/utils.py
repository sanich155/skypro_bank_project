import json
import os

from logs import utils_logger


def get_trans_list(filename: str) -> list:
    """Получает путь до JSON-файла и возвращает список словарей с транзакциями"""

    try:
        with open(os.path.abspath(filename), "r", encoding="utf-8") as f:
            trans_list = json.load(f)
            utils_logger.debug('файл читается')
            return trans_list
    except Exception:
        utils_logger.error('файл не читается')
        return list()
