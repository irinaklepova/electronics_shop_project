import csv


file_name = 'src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        if len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        cls.all.clear()
        with open(file_name, encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            items = list(reader)
            for item in items:
                ob_item = cls(item['name'], Item.string_to_number(item['price']),
                              Item.string_to_number(item['quantity']))

    @staticmethod
    def string_to_number(line):
        """Статический метод, возвращающий число из числа-строки"""
        num = ''
        for symbol in line:
            if symbol.isdigit() or symbol == ".":
                num += symbol
        return int(float(num))
