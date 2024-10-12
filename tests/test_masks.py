import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_num, hide_num", [("1596837868705199", "1596 83** **** 5199"), ("7158300734726758", "7158 30** **** 6758")]
)
def test_get_mask_card_number(card_num, hide_num):
    assert get_mask_card_number(card_num) == hide_num

def test_get_mask_card_number_raise():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('')

    assert str(exc_info.value) == "Неправильный номер карты"

@pytest.mark.parametrize(
    "account_num, hide_num", [("64686473678894779589", "**9589"), ("73654108430135874305", "**4305")]
)
def test_get_mask_account(account_num, hide_num):
    assert get_mask_account(account_num) == hide_num

def test_get_mask_account_raise():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account('')
    assert str(exc_info.value) == "Неправильный номер счета"