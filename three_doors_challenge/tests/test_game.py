import sys
import unittest
from pathlib import Path

sys.path.append(str(Path.cwd()))
from three_doors_challenge.game import Game


class TestChallenge(unittest.TestCase):
    def test_host_opens_door(self):
        """ Тестироует открытие ведушим двери с козой. """
        game = Game()
        for i in range(1, 21):
            game.hidding_car()
            game.gamer_select_door()
            game.host_opens_door()
            result = game.get_result()            
            with self.subTest(f"check {i}: {result}"):
                self.assertNotIn(result.opened_to_presenter, set([result.car_door, result.selected_door]))
            game.reset()
                
    def test_gamer_opens_same_door(self):
        """ Тестирует открытие игроком той же двери, что и выбрал. """
        game = Game()
        for i in range(1, 21):
            game.hidding_car()
            game.gamer_select_door()
            game.host_opens_door()
            game.gamer_opens_same_door()
            result = game.get_result()            
            with self.subTest(f"check {i}: {result}"):
                self.assertEqual(result.opened_door, result.selected_door)
            game.reset()
    
    def test_gamer_opens_another_door(self):
        """ Тестирует открытие игроком другой двери. """
        game = Game()
        for i in range(1, 21):
            game.hidding_car()
            game.gamer_select_door()
            game.host_opens_door()
            game.gamer_opens_another_door()
            result = game.get_result()            
            with self.subTest(f"check {i}: {result}"):
                self.assertNotIn(result.opened_door, set([result.opened_to_presenter, result.selected_door]))
            game.reset()