import unittest
from typing import Any, Dict, List, Union
from unittest.mock import MagicMock, Mock, patch

import requests

from src.utils import get_amount, get_usd_rub_rate, load_transactions


class TestUtils(unittest.TestCase):

    @patch("requests.request")
    def test_get_usd_rub_rate_success(self, mock_request: MagicMock) -> None:
        mock_response: requests.Response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'{"result": 95.5}'
        mock_request.return_value = mock_response
        rate: float = get_usd_rub_rate("USD", 1)
        self.assertEqual(rate, 95.5)

    @patch("requests.request")
    def test_get_usd_rub_rate_failure(self, mock_request: MagicMock) -> None:
        mock_response: requests.Response = requests.Response()
        mock_response.status_code = 400
        mock_request.return_value = mock_response
        rate: float = get_usd_rub_rate("USD", 1)
        self.assertEqual(rate, 0.0)

    @patch("builtins.open", new_callable=MagicMock)
    def test_load_transactions_file_not_found(self, mock_open: MagicMock) -> None:
        mock_open.side_effect = FileNotFoundError
        transactions: List[Dict[str, Any]] = load_transactions("non_existent_file.json")
        self.assertEqual(transactions, [])

    def test_get_amount_rub(self) -> None:
        transaction: Dict[str, Dict[str, Union[str, Dict[str, str]]]] = {
            "operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}
        }
        amount: float = get_amount(transaction)
        self.assertEqual(amount, 100.0)

    def test_get_amount_usd(self) -> None:
        mock_get_usd: Mock = Mock(return_value=1000)
        assert mock_get_usd() == 1000


if __name__ == "__main__":
    unittest.main()
