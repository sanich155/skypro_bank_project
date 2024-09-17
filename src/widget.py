from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_acc_num: str) -> str:
    """Скрывает номер карты или счета"""
    if card_acc_num.split()[0] == "Счет":
        hide_info = card_acc_num.split()[0] + " " + get_mask_account(card_acc_num.split()[1])
    else:
        hide_info = " ".join(card_acc_num.split()[:-1]) + " " + get_mask_card_number(card_acc_num.split()[-1])

    return hide_info


def get_date(format_time: str) -> str:
    """Возвращает дату в виде строки из строки в iso-формате"""
    return datetime.fromisoformat(format_time).strftime("%d.%m.%Y")


test_list = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

for i in test_list:
    print(mask_account_card(i))

print(get_date("2024-03-11T02:26:18.671407"))
