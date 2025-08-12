from dataclasses import dataclass
import random

@dataclass(frozen=True)
class GameResult:
    # Номер двери с автомобилем.
    car_door: int
    # Выбранная дверь.
    selected_door: int
    # Дверь открытая ведущим
    opened_to_presenter: int
    # В результате открытая дверь.
    opened_door: int

class Game:
    def __init__(self):
        # Номер двери с автомобилем.
        self._car_door = 0
        # Выбранная дверь.
        self._selected_door = 0
        # Дверь открытая ведущим.
        self._opened_to_presenter = 0
        # В результате открытая дверь.
        self._opened_door = 0

    def _hidding_car(self):
        """ Прячет автомобиль за дверью. """
        self._car_door = random.randint(1, 3)

    def _gamer_select_door(self):
        """ Игрок выбирает случайную дверь. """
        self._selected_door = random.randint(1, 3)

    def _host_opens_door(self):
        """ Ведущий открывает дверь  с козой. """
        doors = set(range(1, 4))
        # Из выбора удаляется дверь с автомобитлем.        
        doors.discard(self._car_door)
        # Из выбора удаляется дверь выбранная игроком.        
        doors.discard(self._selected_door)
        self._opened_to_presenter = random.choice(tuple(doors))

    def _reset(self):
        """ Сброс выбора. """
        self._car_door = 0
        self._selected_door = 0
        self._opened_to_presenter = 0
        self._opened_door = 0

    @property
    def _result(self) -> GameResult:
        """ Возвращает результаты """
        game_result = GameResult(self._car_door, self._selected_door, self._opened_to_presenter, self._opened_door)
        self._reset()
        return game_result

    def gamer_opens_same_door(self) -> GameResult:
        """ Игрок окрывает туже дверь. """
        self._hidding_car()
        self._gamer_select_door()
        self._host_opens_door()
        self._opened_door = self._selected_door
        return self._result

    def gamer_opens_another_door(self) -> GameResult:
        """ Игрок открывает другую дверь. """
        self._hidding_car()
        self._gamer_select_door()
        self._host_opens_door()
        self._opened_door = (set(range(1, 4)) - set([self._selected_door, self._opened_to_presenter])).pop()
        return self._result
