import unittest

#from project.card.card_repository import CardRepository
#from project.card.magic_card import MagicCard

from Personal_Projects.Players_and_Monsters_Game.project.card.card_repository import CardRepository
from Personal_Projects.Players_and_Monsters_Game.project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_attr_are_set(self):
        card_repo = CardRepository()
        self.assertEqual(card_repo.count, 0)
        self.assertEqual(card_repo.cards, [])

    def test_add_method_raise_ex_when_card_already_exist(self):
        with self.assertRaises(Exception) as ex:
            card_repo = CardRepository()
            mc = MagicCard('test')
            card_repo.add(mc)
            card_repo.add(mc)

        self.assertIsNotNone(ex.exception)

    def test_add_method_add_card_when_unique(self):
        card_repo = CardRepository()
        mc = MagicCard('test')
        mc2 = MagicCard('test2')
        card_repo.add(mc)
        card_repo.add(mc2)
        self.assertEqual(2, card_repo.count)

    def test_remove_method_remove_card(self):
        card_repo = CardRepository()
        mc = MagicCard('test')
        card_repo.add(mc)
        card_repo.remove('test')

    def test_find_card_method(self):
        card_repo = CardRepository()
        mc = MagicCard('test')
        card_repo.add(mc)
        card_repo.find('test')


if __name__ == '__main__':
    unittest.main()