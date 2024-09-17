def get_mask_card_number(card_num: str) -> str:
    """Скрывает номер карты"""
    card_num_mask = (
        card_num[:4]
        + " "
        + card_num[4:6]
        + "**"
        + " "
        + "****"
        + " "
        + card_num[-4::1]
    )
    return card_num_mask


def get_mask_account(account_num: str) -> str:
    """Скрывает номер счета"""
    account_num_mask = "**" + account_num[-4::1]
    return account_num_mask


print(get_mask_card_number("123456789012"))
print(get_mask_account("2184892375942739574829343"))
