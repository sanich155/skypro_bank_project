from logs import masks_logger


def get_mask_card_number(card_num: str) -> str:
    """Скрывает номер карты"""
    if len(card_num) == 16:
        card_num_mask = card_num[:4] + " " + card_num[4:6] + "**" + " " + "****" + " " + card_num[-4::1]
    else:
        masks_logger.error(f'Введен неправильный номер карты: {card_num}')
        raise ValueError("Неправильный номер карты")
    masks_logger.info('C номером карты всё Ок')
    return card_num_mask


def get_mask_account(account_num: str) -> str:
    """Скрывает номер счета"""
    if len(account_num) == 20:
        account_num_mask = "**" + account_num[-4::1]
        masks_logger.warning('Здесь всё работает! Надо же!')
    else:
        masks_logger.critical('Вот так нормально')
        raise ValueError("Неправильный номер счета")
    return account_num_mask
