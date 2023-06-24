import pytest
from src.item import Item


@pytest.fixture
def test_calculate_total_price():
    sofia = Item('Sofia', 3400, 5)
    assert sofia.calculate_total_price() == 17000


def test_apply():
    sofia = Item('Sofia', 3400, 5)
    Item.pay_rate = 0.2
    sofia.apply_discount()
    assert Item.price == 680