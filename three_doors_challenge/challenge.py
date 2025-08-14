import os
import platform

from game import Game

CLEAR_COMMAND = 'clear' if platform.system() == 'Linux' else "cls"
TITLE = "*** Статистика парадокса Монти Холла. ***"

class Challenge:
    def __init__(self) -> None:
        self._game = Game()
    
    def start_console(self):
        """ Запускает консоль. """
        while True:
            self._clear_display()
            print(TITLE)
            self._show_menu()
            action_num = input("Выбериет пункт меню: ").strip(' .').lower()
            if action_num in ('q', 'quit'):
                break
            self._actions_handle(action_num)        

    def _show_menu(self):
        """ Отображает меню действий. """
        print("1. Запустить статистики при смене двери.")
        print('2. Запустить статистику при выборе той же дери.')
        print(f"(q)uit. Выход.")
        print("")

    def _actions_handle(self, action_num: str):
        actions = {
            '1': self._gamer_opens_another_door,
            '2': self._gamer_opens_some_door}
        actions[action_num]()
   
    def _gamer_opens_another_door(self):
        """ Запуск имитации октрытия в игре другой двери. """
        self._gamer_opens_door(True)
    
    def _gamer_opens_some_door(self):
        """ Запуск имитации октрытия в игре той же двери. """
        self._gamer_opens_door(False)

    def _gamer_opens_door(self, is_another: bool) -> int:
        """
        Запуск имитации октрытия двери много раз со сбором статистики.
        :param is_another: Еслим True, то условие "Открывает другую дверь", иначе "Ту же дверь что и выбрал изначально".
        """
        right = 0                           # Количество верно открытых дверей.
        count = self._input_cicle_count()   # Общее количество открываемых дверей.
        for i in range(count):
            result = self._game.gamer_opens_another_door() if is_another else self._game.gamer_opens_same_door()
            if result.opened_door == result.car_door:
                right += 1
        percent = 100 / count * right
        print(f" Процент верного угадывания при открытии {count} раз {'другой' if is_another else 'той же'} двери равен {percent:.0f}%.")
        input("Нажмите любую клавишу...")
    
    def _input_cicle_count(self):
        """ Запрос количеств циклов """
        while True:
            try:
                count = int(input("Сколько раз требуется произвести имитацию: "))
                if count < 1:
                    print("Количество должнл быть больше нуля")
                else:
                    return count                
            except ValueError:
                print("Значение должно быть целым числом")

    def _clear_display(self):
        """ Очищает дисплей. """
        os.system(CLEAR_COMMAND)

if __name__ == "__main__":
    challenge = Challenge()
    challenge.start_console()
