import random

class Challenge:
    def __init__(self):
        # Номер двери с автомобилем.
        self._car_door = 0
        # Выбранная дверь.
        self._selected_door = 0
        # Дверь открытая ведущим.
        self._opened_to_presenter = 0
        # В результате открытая дверь.
        self._opened_door = 0

    def hiding_car(self):
        """ Прячет автомобиль за дверью. """
        self._car_door = random.randint(1, 3)

    def selecting_door(self):
        """ Выбирает случайную дверь """
        self._selected_door = random.randint(1, 3)

    def host_opens_door(self):
        """ Ведущий открывает дверь """
        pass