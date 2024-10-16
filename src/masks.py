def get_mask_card_number(card_num: str) -> str:
    """Скрывает номер карты"""
    if len(card_num) == 16:
        card_num_mask = card_num[:4] + " " + card_num[4:6] + "**" + " " + "****" + " " + card_num[-4::1]
    else:
        raise ValueError("Неправильный номер карты")
    return card_num_mask


def get_mask_account(account_num: str) -> str:
    """Скрывает номер счета"""
    if len(account_num) == 20:
        account_num_mask = "**" + account_num[-4::1]
    else:
        raise ValueError("Неправильный номер счета")
    return account_num_mask
