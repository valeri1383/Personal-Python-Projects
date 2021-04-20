import unittest

#from Personal_Projects.Players_and_Monsters_Game.project.card.trap_card import TrapCard
from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_attr_are_set(self):
        tc = TrapCard('test')
        self.assertEqual(tc.name, 'test')
        self.assertEqual(tc.damage_points, 120)
        self.assertEqual(tc.health_points, 5)

    def test_name_raise_exemption_when_empty(self):
        with self.assertRaises(Exception) as ex:
            tc = TrapCard('')

        self.assertIsNotNone(ex.exception)

    def test_damage_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            tc = TrapCard('test')
            tc.damage_points = -5

        self.assertIsNotNone(ex.exception)

    def test_health_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            tc = TrapCard('test')
            tc.health_points = -5

        self.assertIsNotNone(ex.exception)


if __name__ == '__main__':
    unittest.main()