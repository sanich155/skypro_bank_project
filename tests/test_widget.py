import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Проверяет сокрытие номера счета или карты"""
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_exc() -> None:
    """Проверяет функцию сокрытия номера счета/карты, если номера нет или он неверен"""
    with pytest.raises(Exception) as exc_info:
        mask_account_card("")
    assert str(exc_info.value) == "Отсутствует номер карты/счета"


def test_get_data() -> None:
    """Првоеряет функцию смены формата даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("1999-11-11T04:22:39.328483") == "11.11.1999"
    assert get_date("1999-11-T04:22:39.328483") == ""
    assert get_date("") == ""
