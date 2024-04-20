import pytest

from src.masks import account_mask, card_mask


@pytest.fixture
def bill_num() -> str:
    return "1234567890"


def test_account_mask(bill_num: str) -> None:
    assert account_mask(bill_num) == "**7890"


@pytest.mark.parametrize(
    "card_num, mask_card_num", [("1234567887654321", "1234 56** **** 4321"), ("1111111111111111", "1111 11** **** 1111")]
)
def test_card_mask(card_num: str, mask_card_num: str) -> None:
    assert card_mask(card_num) == mask_card_num
