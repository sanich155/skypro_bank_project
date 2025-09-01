from unittest.mock import Mock
from unittest.mock import patch
from src.utils import get_trans_list

@patch('builtins.open', create=True)
def test_get_trans_list(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = 'test data'
    assert get_trans_list('test.txt') == 'test data'
    mock_open.assert_called_once_with('test.txt', 'r')

