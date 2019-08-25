"""
Возвращаем массив в случайном порядке
# по факту это бред
ответ просто
random.sample(array, len(array))

"""

import unittest
import random


class RandomIterator:
    def __init__(self, array: list):
        self.array = array
        self.index = 0
        self.populated = random.sample(range(len(array)), len(array))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.array):
            result = self.array[self.populated[self.index]]
            self.index += 1
            return result
        else:
            raise StopIteration


def random_generator(array):
    populated = random.sample(array, len(array))
    for i in populated:
        yield array[i]


class RandomIteratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.array = list(range(10))

    def test_random(self):
        random.seed(0)
        expected = random.sample(self.array, len(self.array))
        random.seed(0)

        self.assertEqual(expected, list(RandomIterator(self.array)))

    def test_random_generator(self):
        random.seed(0)
        expected = random.sample(self.array, len(self.array))
        random.seed(0)
        actual = list(random_generator(self.array))

        self.assertEqual(expected, actual)
