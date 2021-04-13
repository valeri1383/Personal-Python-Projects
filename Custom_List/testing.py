import unittest
from Personal_Projects.Custom_List.custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomList('a', 2, 'dfg', 5)

    def test_custom_append_method(self):
        result = self.custom_list.append(7)
        self.assertEqual(['a', 2, 'dfg', 5, 7], result)

    def test_remove_when_index_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.remove(120)

        self.assertIsNotNone(ex.exception)

    def test_remove_when_index_not_int(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.remove('a')

        self.assertIsNotNone(ex.exception)

    def test_remove_when_index_valid(self):
        result = self.custom_list.remove(1)
        self.assertEqual(result, 2)

    def test_get_when_index_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.get(45)

        self.assertIsNotNone(ex.exception)

    def test_get_when_index_not_int(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.get('a')

        self.assertIsNotNone(ex.exception)

    def test_get_when_index_valid(self):
        result = self.custom_list.get(0)
        self.assertEqual(result, 'a')

    def test_extend_method(self):
        result = self.custom_list.extend(['v', 5])
        self.assertEqual(result, ['a', 2, 'dfg', 5, 'v', 5])

    def test_insert_method(self):
        result = self.custom_list.insert(2, 'opa')
        updated_list = ['a', 2, 'opa', 'dfg', 5]
        self.assertEqual(updated_list, result)

    def test_pop_when_list_is_empty_throw_error(self):
        self.custom_list = CustomList()
        with self.assertRaises(Exception) as ex:
            self.custom_list.pop()

        self.assertIsNotNone(ex.exception)

    def test_pop_when_valid(self):
        result = self.custom_list.pop()
        self.assertEqual(result, 5)

    def test_clear_method(self):
        self.custom_list.clear()
        self.assertEqual([], self.custom_list.reverse())

    def test_index_when_exist(self):
        result = self.custom_list.index('a')
        self.assertEqual(0, result)

    def test_index_when_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.index('b')

        self.assertIsNotNone(ex.exception)

    def test_count_when_value_exist(self):
        result = self.custom_list.count('a')
        self.assertEqual(result, 1)

    def test_count_when_value_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.count('b')

        self.assertIsNotNone(ex.exception)

    def test_reverse_method(self):
        result = self.custom_list.reverse()
        self.assertEqual([5, 'dfg', 2, 'a'], result)

    def test_copy_method(self):
        result = self.custom_list.copy()
        self.assertEqual(result.reverse(), self.custom_list.reverse())

    def test_size_method(self):
        result = self.custom_list.size()
        self.assertEqual(4, result)

    def test_add_first_method(self):
        value = (1, 2, 3)
        self.custom_list.add_first(value)
        self.assertEqual([1, 2, 3, 'a', 2, 'dfg', 5], self.custom_list.reverse()[::-1])

    def test_dictionize_when_element_are_even(self):
        result = self.custom_list.dictionize()
        self.assertEqual(result, {'a': 2, 'dfg': 5})

    def test_dictionize_when_element_are_odd(self):
        self.custom_list.extend([9])
        self.assertEqual(self.custom_list.dictionize(), {'a': 2, 'dfg': 5, 9: ''})

    def test_move_method_when_amount_is_valid(self):
        result = self.custom_list.move(2)
        self.assertEqual(result, ['dfg', 5, 'a', 2])

    def test_move_method_when_amount_is_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.custom_list.move('a')

        self.assertIsNotNone(ex.exception)

    def test_sum_method(self):
        result = self.custom_list.sum()
        self.assertEqual(result, 11)

    def test_overbound_method_return_idex_of_element(self):
        # 'a', 2, 'dfg', 5
        result = self.custom_list.overbound()
        self.assertEqual(result, 3)

    def test_underbound_method_return_idex_of_element(self):
        # 'a', 2, 'dfg', 5
        result = self.custom_list.underbound()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()