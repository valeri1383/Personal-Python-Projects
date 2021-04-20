import unittest

#from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner
from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_set_attr(self):
        beginner = Beginner('test')
        self.assertEqual(beginner.username, 'test')
        self.assertEqual(beginner.health, 50)

    def test_name_raise_exemption_when_empty_str(self):
        with self.assertRaises(Exception) as ex:
            beginner = Beginner('')

        self.assertIsNotNone(ex.exception)

    def test_health_raise_exemption_when_lower_than_0(self):
        with self.assertRaises(Exception) as ex:
            beginner = Beginner('test')
            beginner.health = -5

        self.assertIsNotNone(ex.exception)

    def test_is_dead_return_True_when_health_less_than_0(self):
        beginner = Beginner('test')
        beginner.health = 0
        self.assertEqual(beginner.is_dead, True)

    def test_take_damage_raise_ex_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            beginner = Beginner('test')
            beginner.take_damage(-3)

        self.assertIsNotNone(ex.exception)

    def test_take_damage_lower_the_health_when_positive_number(self):
        beginner = Beginner('test')
        beginner.take_damage(10)
        self.assertEqual(beginner.health, 40)


if __name__ == '__main__':
    unittest.main()