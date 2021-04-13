class CustomListIndexException(Exception):
    pass


class CustomListTypeException(Exception):
    pass


class CustomListValueException(Exception):
    pass


class CustomListSumException(Exception):
    pass


class CustomList:
    def __init__(self, *args):
        self.custom_list = [el for el in args]

    def append(self, value):
        self.custom_list = self.custom_list + [value]
        return self.custom_list

    def remove(self, index):
        try:
            value = self.custom_list[index]
            del self.custom_list[index]
            return value

        except IndexError:
            raise CustomListIndexException("Custom list doesn't contain element with this index")

        except TypeError:
            raise CustomListTypeException(f'Index argument does not mach the supported type. Should be integer it was {type(index)}')

    def get(self, index):
        try:
            value = self.custom_list[index]
            return value

        except IndexError:
            raise CustomListIndexException("Custom list doesn't contain element with this index")

        except TypeError:
            raise CustomListTypeException(f'Index argument does not mach the supported type. Should be integer it was {type(index)}')

    def extend(self, iterable):
        self.custom_list = self.custom_list + [*iterable]
        return self.custom_list

    def insert(self, index, value):
        self.custom_list = self.custom_list[:index] + [value] + self.custom_list[index:]
        return self.custom_list

    def pop(self):
        try:
            el = self.custom_list[-1]
            del self.custom_list[-1]
            return el
        except IndexError:
            raise CustomListIndexException('List is empty')

    def clear(self):
        self.custom_list = []

    def index(self, value):
        if value in self.custom_list:
            for i in range(len(self.custom_list)):
                if self.custom_list[i] == value:
                    return i
        else:
            raise CustomListIndexException("Custom list doesn't contain element with this index")

    def count(self, value):
        if value in self.custom_list:
            counter = 0
            for el in self.custom_list:
                if el == value:
                    counter += 1
            return counter
        else:
            raise CustomListValueException("Custom list doesn't contain the given value")

    def reverse(self):
        return self.custom_list[::-1]

    def copy(self):
        copy = CustomList(*self.custom_list)
        return copy

    def size(self):
        return len(self.custom_list)

    def add_first(self, value):
        self.custom_list = [*value] + self.custom_list

    def dictionize(self):
        custom_dict = {}
        for index in range(0, len(self.custom_list), 2):
            try:
                custom_dict[self.custom_list[index]] = self.custom_list[index + 1]
            except IndexError:
                custom_dict[self.custom_list[index]] = ''
        return custom_dict

    def move(self, amount):
        try:
            part = self.custom_list[:amount]
            self.custom_list = self.custom_list[amount:] + part
            return self.custom_list

        except TypeError:
            raise CustomListTypeException(f'Index argument does not mach the supported type. Should be integer it was {type(amount)}')

    def sum(self):
        result = 0
        for el in self.custom_list:
            if isinstance(el, int) or isinstance(el, float):
                result += el
                continue
            try:
                result += len(el)
            except TypeError:
                raise CustomListSumException("Please provide a len method to custom objects if you want to sum elements.")

        return result

    def overbound(self):
        max_num = float('-inf')
        element = None
        for el in self.custom_list:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if num > max_num:
                max_num = num
                element = el
        return self.index(element)

    def underbound(self):
        min_num = float('inf')
        element = None
        for el in self.custom_list:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if num < min_num:
                min_num = num
                element = el
        return self.index(element)
