import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_num, hide_num', [('1596837868705199', '1596 83** **** 5199'), ('7158300734726758', '7158 30** **** 6758')])
def test_get_mask_card_number(card_num, hide_num):
    assert get_mask_card_number(card_num) == hide_num

