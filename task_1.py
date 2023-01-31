class Game:
    def __init__(self, name: str, cost: int):
        """
        Создание и подготовка к работе объекта "Игра"
        :param name: Имя игры
        :param сost: Стоимость игры
        Примеры:
        >>> game = Game("Прятки", 0)
        """
        if not isinstance(name, str):  # проверяем, что имя игры типа str
            raise TypeError('Пожалуйста, введите строковое значение')  # вызываем ошибку
        if len(name) == 0:  # проверяем, что существует значение в имени
            raise ValueError('Пожалуйста, напишите значение')  # вызываем ошибку
        self._name = name
        self.cost = cost

    def __str__(self) -> str:
        return f"Игра {self.name}. Стоимость {self.cost}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, cost={self.cost!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def cost(self) -> int:
        return self._cost

    @cost.setter
    def cost(self, new_cost) -> None:
        if not isinstance(new_cost, int):  # проверяем, что стоимость игры типа int
            raise TypeError('Пожалуйста, введите целочисленное значение')  # вызываем ошибку
        if new_cost < 0:  # проверяем, что стоимость игры не меньше нуля (0 можно, если игра продаётся бесплатно)
            raise ValueError(
                'Простите, но cтоимость не может быть ниже нуля')  # вызываем ошибку
        self._cost = new_cost  # вызываем ошибку

    def play(self) -> str:
        """
        Функция которая указывает на то, что в игру можно играть
        :return: метод возвращает строку "Игра {название_игры} готова приносить удовольствие"
        Примеры:
        >>> game = Game("Прятки", 0)
        >>> game.play()
        """
        return f'Игра {self.name} готова приносить удовольствие '

    def sell(self) -> str:
        """
        Функция указывающая на обновление информации о продаже игры
        :return: метод возвращает строку "Информация о продаже игры обновлена. Игра
         {название_игры} продаётся на авито за {стоимость_игры} рублей"
        Примеры:
        >>> game = Game("Прятки", 0)
        >>> game.sell()
        """
        return f'Информация о продаже игры обновлена. Игра {self.name} продаётся на авито за {self.cost} рублей'


class VideoGame(Game):
    def __init__(self, name: str, cost: int, platform: str):
        """
        Создание и подготовка к работе объекта "Видеоигра"
        :param name: Имя игры
        :param сost: Стоимость игры
        :param platform: Платформа на которой игра работает
        Примеры:
        >>> hades = VideoGame("Hades", 918, 'PC')
        """
        super().__init__(name, cost)
        self.platform = platform

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, cost={self.cost!r} platform={self.platform!r})"

    @property
    def platform(self) -> str:
        return self._platform

    @platform.setter
    def platform(self, new_platform) -> None:
        if not isinstance(new_platform, str):  # проверяем, что платформа игры типа str
            raise TypeError('Пожалуйста, введите строковое значение')  # вызываем ошибку
        if len(new_platform) == 0:  # проверяем, что есть значение в платформе игры не равно пустой строке
            raise ValueError('Пожалуйста, напишите значение')  # вызываем ошибку
        self._platform = new_platform

    def play(self) -> str:
        """
        Функция которая указывает на то, что платформа игры запущена
        И в игрой можно пользоваться.
        :return: метод возвращает строку "{Платформа_игры} включен. Игра {название_игры} готова приносить удовольствие"
        Примеры:
        >>> hades = VideoGame("Hades", 918, 'PC')
        >>> hades.play()
        """
        platform_ready = f'{self.platform} включен.'
        game_ready = super().play()
        return f'{platform_ready} {game_ready}'


class BoardGame(Game):
    def __init__(self, name: str, cost: int, friends_count: int):
        """
        Создание и подготовка к работе объекта "Настольная игра"
        :param name: Имя игры
        :param сost: Стоимость игры
        :param friends_count: Количество друзей, с которыми нужно играть
        Примеры:
        >>> manchkin = BoardGame("Manchkin", 2000, 6)
        """
        super().__init__(name, cost)
        self.friends_count = friends_count

    def __str__(self) -> str:
        return f"Настольная игра {self.name}. Стоимость {self.cost}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, cost={self.cost!r} friends={self.friends_count!r})"

    @property
    def friends_count(self) -> int:
        return self._friends_count

    @friends_count.setter
    def friends_count(self, new_friends_count: int) -> None:
        if not isinstance(new_friends_count, int):  # проверяем, что количество дрзей для игры типа int
            raise TypeError('Пожалуйста, введите целочисленное значение')  # вызываем ошибку
        if new_friends_count < 0:  # проверяем, что количество дрзей для игры не меньше нуля (0 разрешен для одиноких)
            raise ValueError('Простите, но количество друзей не может быть ниже нуля')  # вызываем ошибку
        self._friends_count = new_friends_count

    def play(self) -> str:
        """
        Функция которая указывает на то, что друзья пришли
        И в игрой можно пользоваться.
        :return: метод возвращает строку "{Платформа_игры} включен. Игра {название_игры} готова приносить удовольствие"
        Примеры:
        >>> manchkin = BoardGame("Manchkin", 2000, 6)
        >>> manchkin.play()
        """
        friends_ready = f'{self.friends_count} друзей пришло.'
        game_ready = super().play()
        return f'{friends_ready} {game_ready}'
