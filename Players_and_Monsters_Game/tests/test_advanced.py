import unittest

#from Personal_Projects.Players_and_Monsters_Game.project.player.advanced import Advanced
from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_set_attr(self):
        advanced = Advanced('test')
        self.assertEqual(advanced.username, 'test')
        self.assertEqual(advanced.health, 250)

    def test_name_raise_exemption_when_empty_str(self):
        with self.assertRaises(Exception) as ex:
            advanced = Advanced('')

        self.assertIsNotNone(ex.exception)

    def test_health_raise_exemption_when_lower_than_0(self):
        with self.assertRaises(Exception) as ex:
            advanced = Advanced('test')
            advanced.health = -5

        self.assertIsNotNone(ex.exception)

    def test_is_dead_return_True_when_health_less_than_0(self):
        advanced = Advanced('test')
        advanced.health = 0
        self.assertEqual(advanced.is_dead, True)

    def test_take_damage_raise_ex_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            advanced = Advanced('test')
            advanced.take_damage(-3)

        self.assertIsNotNone(ex.exception)

    def test_take_damage_lower_the_health_when_positive_number(self):
        advanced = Advanced('test')
        advanced.take_damage(50)
        self.assertEqual(advanced.health, 200)


if __name__ == '__main__':
    unittest.main()