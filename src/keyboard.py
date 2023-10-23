from src.item import Item


class MixinKeyboard:
    """Класс, реализующий дополнительный функционал по хранению и изменению раскладки клавиатуры"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод для изменения языка"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language


class Keyboard(MixinKeyboard, Item):
    pass
