import unittest

#from Personal_Projects.Hotel_Everland.project.rooms.room import Room
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def test_set_attr(self):
        room = Room('test', 100, 2)
        self.assertEqual(room.family_name, 'test')
        self.assertEqual(room.budget, 100)
        self.assertEqual(room.members_count, 2)
        self.assertEqual(room.children, [])

    def test_expenses_raise_ex_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            room = Room('test', 100, 2)
            room.expenses = -6

        self.assertIsNotNone(ex.exception)

    def test_expenses_set_when_eq_or_more_than_0(self):
        room = Room('test', 100, 2)
        room.expenses = 60
        self.assertEqual(room.expenses, 60)

