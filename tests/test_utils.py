import unittest

# import os
# from pathlib import Path
from typing import Dict
from unittest.mock import Mock, patch

from src.utils import get_amount, get_usd_rub_rate, load_transactions


class TestFunctions(unittest.TestCase):

    @patch("requests.get")
    def test_get_usd_rub_rate(self, mock_currency: Mock) -> None:
        mock_currency.return_value.json.return_value = {"Valute": {"USD": {"Value": "1.00"}}}  # Mocking a response
        self.assertEqual(get_usd_rub_rate("USD", 1), 1.00)

    def test_get_amount(self) -> None:
        dictionary: Dict = {"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.00"}}
        self.assertEqual(get_amount(dictionary), 100.00)

    def test_load_transactions(self) -> None:
        assert load_transactions("../tests/test_operation.json") == []


if __name__ == "__main__":
    unittest.main()
