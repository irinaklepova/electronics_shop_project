"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
file_name = 'src/items.csv'


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



def test_name_setter():
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(file_name)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
