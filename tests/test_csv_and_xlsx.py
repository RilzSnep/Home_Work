import unittest
from typing import Any
from unittest.mock import patch
import pandas as pd
from src.csv_and_xlsx import read_csv, read_xlsx


def test_read_csv() -> None:
    sus = None
    assert read_csv("test_transactions.csv") == sus


@patch("pandas.read_xlsx")
def test_read_xlsx(mock_read_xlsx: Any) -> None:
    """
    Тестирование функционала чтения транзакций из Excel файла.
    """
    mock_read_xlsx.return_value = pd.DataFrame({"Date": ["2022-01-01", "2022-02-01"], "Amount": [100.00, 200.00]})
    result = read_xlsx("../data/transactions_excel.xlsx")
    exp_result = [{"Date": "2022-01-01", "Amount": 100.00}, {"Date": "2022-02-01", "Amount": 200.00}]
    unittest.TestCase().assertEqual(result, exp_result)


if __name__ == "main":
    unittest.main()
