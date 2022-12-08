# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Pillow:
    def __init__(self, width: int, length: int, neet_to_iron: bool):
        """
        Создание и подготовка к работе объекта "Подушка"
        :param width: Ширина подушки
        :param length: Длина подушки
        :param neet_to_iron: Нужно ли гладить подушку
        Примеры:
        >>> pillow = Pillow(100, 100, True)  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)) or not isinstance(length, (int, float)):
            raise TypeError
        self.width = width
        self.length = length
        self.neet_to_iron = neet_to_iron

    def kick_the_pillow(self) -> None:
        """
        Функция которая делает подушкой мятой и меняет значение neet_to_iron на true
        :return: значение need_to_iron становится true
        Примеры:
         >>> pillow = Pillow(100, 100, True)
        >>> pillow.kick_the_pillow()
        """
        ...

    def iron_the_pillow(self) -> None:
        """
        Функция которая делает подушку глаженной
        :raise ValueError: Если подушку гладить не надо, то возвращается ошибка.
        :return: значение need_to_iron становится false
        Примеры:
         >>> pillow = Pillow(100, 100, True)
        >>> pillow.iron_the_pillow()
        """
        ...


class Food:
    def __init__(self, proteint: Union[int, float], carbs: Union[int, float], fat: Union[int, float]):
        if not isinstance(proteint, (int, float)) or not isinstance(carbs, (int, float)) or not isinstance(fat, (
                int, float)):
            raise TypeError
        self.proteint = proteint
        self.carbs = carbs
        self.fat = fat

    def is_food_healthy(self) -> bool:
        """
        Функция которая проверяет каллорийность продукта: углеводы + белки умножить на 4, жир на 9
        :return: если калорийность выше значения 600, то выдаёт false, иначе true
        Примеры:
        >>> protein_bar = Food(20, 17, 10)
        >>> protein_bar.is_food_healthy()
        """
        ...

    def is_food_for_muscle_growth(self):
        """
        Функция которая проверяет, чего больше: углеводов или белка
        :return: если углеводов, то выдаёт false, иначе true
        Примеры:
        >>> protein_bar = Food(20, 17, 10)
        >>> protein_bar.is_food_for_muscle_growth()
        """
        ...

    def is_food_worth_buying(self):
        """
        Функция которая вызывает функции  is_food_for_muscle_growth и is_food_healthy
        :return: если оба дают true - метод возвращает "берите конечно!",
                 если is_food_for_muscle_growth == false - метод возвращает "можно, если белки не важны",
                 иначе метод возвращает "не стоит твоего внимания"
        Примеры:
        >>> protein_bar = Food(20, 17, 10)
        >>> protein_bar.is_food_worth_buying()
        """


class Game:
    def __init__(self, worthiness: Union[int, float], price: int):
        if not isinstance(price, int) or not isinstance(worthiness, (int, float)):
            raise TypeError
        self.worthiness = None
        self.init_worthiness(worthiness)
        self.price = price

    def init_worthiness(self, worthiness: Union[int, float]) -> None:
        """
        Функция которая провверяет, чтобы ценность не было больше 10
        :raise ValueError: Если ценность больше 10, то возвращается ошибка.
        :return: передаёт значение self.worthiness
        Примеры:
         >>> the_calisto_protocol = Game(6, 4000)
        """
        if worthiness > 10:
            raise ValueError
        self.worthiness = worthiness

    def should_play(self) -> bool:
        """
        Функция которая вызывает функции  is_food_for_muscle_growth и is_food_healthy
        :return: если ценность больше 8 и цена ниже 1500, возвращает true, иначе false
        Примеры:
        >>> the_calisto_protocol = Game(6, 4000)
        >>> the_calisto_protocol.should_play()
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
