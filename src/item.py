import csv
import os.path
from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = 'items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name  # атрибут `name` сделать приватным
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """Магический метод `__repr__` (для разработчика)"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод `__str__` (для пользователя)"""
        return f"{self.__name}"

    def __add__(self, other):
        """Магический метод для сложения объектов класса"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты класса Item и его наследников")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    """добавить геттер и сеттер для `name`, используя @property"""
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        """В сеттере `name` проверять, что длина наименования товара не больше 10 символов.
            В противном случае, обрезать строку (оставить первые 10 символов)"""
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        src_file = os.path.join(os.path.dirname(__file__), cls.file_name)
        cls.all.clear()
        try:
            with open(src_file, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                items = list(reader)
                for item in items:
                    cls.check_columns(item)  # проверяем ряд в таблице на наличие всех необходимых столбцов
                    cls(item['name'], Item.string_to_number(item['price']),
                        Item.string_to_number(item['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls.file_name}')
        except InstantiateCSVError:
            raise InstantiateCSVError(cls.file_name)

    @classmethod
    def check_columns(cls, row):
        """Класс-метод для проверки названий столбцов"""
        if not('name' in row and 'price' in row and 'quantity' in row):
            raise InstantiateCSVError(cls.file_name)

    @staticmethod
    def string_to_number(line):
        """Статический метод, возвращающий число из числа-строки"""
        num = ''
        for symbol in line:
            if symbol.isdigit() or symbol == ".":
                num += symbol
        return int(float(num))
