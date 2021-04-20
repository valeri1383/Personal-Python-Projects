import unittest

# from Personal_Projects.Players_and_Monsters_Game.project.card.card_repository import CardRepository
# from Personal_Projects.Players_and_Monsters_Game.project.card.magic_card import MagicCard
# from Personal_Projects.Players_and_Monsters_Game.project.controller import Controller
# from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner
# from Personal_Projects.Players_and_Monsters_Game.project.player.player_repository import PlayerRepository

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.player_repo = PlayerRepository()
        self.card_repo = CardRepository()
        self.controller = Controller()

    def test_adding_new_player(self):
        result = self.controller.add_player('Beginner', 'test')
        self.assertEqual(result, "Successfully added player of type Beginner with username: test")

    def test_adding_new_card(self):
        result = self.controller.add_card('Trap', 'test')
        self.assertEqual(result, "Successfully added card of type TrapCard with name: test")


if __name__ == '__main__':
    unittest.main()