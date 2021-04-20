import unittest

#from Personal_Projects.Players_and_Monsters_Game.project.card.magic_card import MagicCard
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_attr_are_set(self):
        mc = MagicCard('test')
        self.assertEqual(mc.name, 'test')
        self.assertEqual(mc.damage_points, 5)
        self.assertEqual(mc.health_points, 80)

    def test_name_raise_exemption_when_empty(self):
        with self.assertRaises(Exception) as ex:
            mc = MagicCard('')

        self.assertIsNotNone(ex.exception)

    def test_damage_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            mc = MagicCard('test')
            mc.damage_points = -5

        self.assertIsNotNone(ex.exception)

    def test_health_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            mc = MagicCard('test')
            mc.health_points = -5

        self.assertIsNotNone(ex.exception)


if __name__ == '__main__':
    unittest.main()