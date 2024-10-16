from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_acc_num: str) -> str:
    """Скрывает номер карты или счета"""
    if card_acc_num == "":
        raise Exception("Отсутствует номер карты/счета")
    elif card_acc_num.split()[0] == "Счет":
        hide_info = card_acc_num.split()[0] + " " + get_mask_account(card_acc_num.split()[-1])
    else:
        hide_info = " ".join(card_acc_num.split()[:-1]) + " " + get_mask_card_number(card_acc_num.split()[-1])
    return hide_info


def get_date(format_time: str) -> str:
    """Возвращает дату в виде строки из строки в iso-формате"""
    try:
        return datetime.fromisoformat(format_time).strftime("%d.%m.%Y")
    except ValueError as e:
        print(e)
        return ""
