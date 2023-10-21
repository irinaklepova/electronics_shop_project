from src.phone import Phone
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
phone1 = Phone('iPhone 14', 120000, 5, 2)


def test_init():
    """Тест методов str и repr"""
    assert str(phone1) == "iPhone 14"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_add():
    """Тест метода add"""
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

