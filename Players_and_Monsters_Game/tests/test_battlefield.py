import unittest

# from Personal_Projects.Players_and_Monsters_Game.project.battle_field import BattleField
# from Personal_Projects.Players_and_Monsters_Game.project.card.magic_card import MagicCard
# from Personal_Projects.Players_and_Monsters_Game.project.card.trap_card import TrapCard
# from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner

class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battle_field = BattleField()
        self.attacker = Beginner('attacker')
        self.enemy = Beginner('enemy')

    def test_fight_raise_ex_when_attacker_is_dead(self):
        with self.assertRaises(Exception) as ex:
            self.attacker.health = 0
            self.battle_field.fight(self.attacker, self.enemy)

        self.assertIsNotNone(ex.exception)

    def test_fight_raise_ex_when_enemy_is_dead(self):
        with self.assertRaises(Exception) as ex:
            self.enemy.health = 0
            self.battle_field.fight(self.attacker, self.enemy)

        self.assertIsNotNone(ex.exception)

    def test_fight_raise_attacker_health_when_beginner(self):
        self.battle_field.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 90)

    def test_fight_raise_enemy_health_when_beginner(self):
        self.battle_field.fight(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 90)

    def test_fight_raise_card_damage_points_when_beginner(self):
        magic_card = MagicCard('test')
        trap_card2 = TrapCard('test2')
        self.attacker.card_repository.add(magic_card)
        self.attacker.card_repository.add(trap_card2)
        total_cards = [x.damage_points + 30 for x in self.attacker.card_repository.cards]
        self.assertEqual([35, 150], total_cards)

    def test_fight_raise_attacker_health_with_sum_of_cards_health(self):
        magic_card = MagicCard('test')
        trap_card2 = TrapCard('test2')
        self.attacker.card_repository.add(magic_card)
        self.attacker.card_repository.add(trap_card2)
        sum_card_health = sum([x.health_points for x in self.attacker.card_repository.cards])
        self.assertEqual(135, sum_card_health + self.attacker.health)

    def test_fight_raise_enemy_health_with_sum_of_cards_health(self):
        magic_card = MagicCard('test')
        trap_card2 = TrapCard('test2')
        self.enemy.card_repository.add(magic_card)
        self.enemy.card_repository.add(trap_card2)
        sum_card_health = sum([x.health_points for x in self.enemy.card_repository.cards])
        self.assertEqual(135, sum_card_health + self.enemy.health)

    def test_attacker_damage_enemy(self):
        trap_card = TrapCard('attacker')
        magic_card2 = MagicCard('enemy')
        self.attacker.card_repository.add(trap_card)
        self.enemy.card_repository.add(magic_card2)
        self.battle_field.fight(self.attacker, self.enemy)
        self.assertEqual(20, self.enemy.health)
        self.assertEqual(60, self.attacker.health)

    def test_enemy_damage_attacker(self):
        trap_card = TrapCard('attacker')
        magic_card2 = MagicCard('enemy')
        self.attacker.card_repository.add(trap_card)
        self.enemy.card_repository.add(magic_card2)
        self.battle_field.fight(self.attacker, self.enemy)
        self.assertEqual(60, self.attacker.health)


if __name__ == '__main__':
    unittest.main()