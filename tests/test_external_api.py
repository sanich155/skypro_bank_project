from unittest.mock import patch
from src.external_api import convert
from src.utils import get_trans_list

@patch('requests.get')
def test_convert(mock_get):
    mock_get.return_value.json.return_value = {'info': {'timestamp': 1760915524, 'rate': 81.419391}, 'date': '2025-10-19', 'result': 799869.796541}
    assert convert(get_trans_list('data/operations.json')[2]) == 799869.8

