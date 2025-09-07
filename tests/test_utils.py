from unittest.mock import Mock
from unittest.mock import patch
from src.utils import get_trans_list
import os

def test_get_trans_list():
    assert get_trans_list(os.path.abspath("data/lol.json")) == []
    assert get_trans_list(os.path.abspath("data/operations.json"))[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }


