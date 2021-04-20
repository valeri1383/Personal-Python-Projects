import unittest

#from Personal_Projects.Players_and_Monsters_Game.project.player.player_repository import PlayerRepository
#from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner

from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner


class TestPlayerRepository(unittest.TestCase):
    def test_attr_are_set(self):
        player_repo = PlayerRepository()
        self.assertEqual(player_repo.count, 0)
        self.assertEqual(player_repo.players, [])

    def test_add_method_raise_ex_when_card_already_exist(self):
        with self.assertRaises(Exception) as ex:
            player_repo = PlayerRepository()
            beginner = Beginner('test')
            player_repo.add(beginner)
            player_repo.add(beginner)

        self.assertIsNotNone(ex.exception)

    def test_add_method_add_card_when_unique(self):
        player_repo = PlayerRepository()
        beginner = Beginner('test')
        beginner2 = Beginner('test2')
        player_repo.add(beginner)
        player_repo.add(beginner2)
        self.assertEqual(2, player_repo.count)

    def test_remove_method_remove_card(self):
        player_repo = PlayerRepository()
        beginner = Beginner('test')
        player_repo.add(beginner)
        player_repo.remove('test')

    def test_find_card_method(self):
        player_repo = PlayerRepository()
        beginner = Beginner('test')
        player_repo.add(beginner)
        player_repo.find('test')


if __name__ == '__main__':
    unittest.main()
