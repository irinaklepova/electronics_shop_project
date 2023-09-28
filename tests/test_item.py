"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_ob():
    return Item("Наушники", 200, 100)


def test_item_init(item_ob):
    assert item_ob.name == "Наушники"


def test_calculate_total_price(item_ob):
    assert item_ob.calculate_total_price() == 20000


def test_apply_discount(item_ob):
    item_ob.apply_discount()
    assert item_ob.price == 200 * item_ob.pay_rate
