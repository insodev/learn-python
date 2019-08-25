"""
Есть файл, в котором содержаться слова разделённые пробелом. Например:
"abba com mother bill mother com abba dog abba mother com".
Нужно найти и вывести тройку слов, которые чаще всего встречаются вместе (порядок не имеет значения).
То есть в моём примере тройки слов это "abba com mother", "com mother bill", "mother bill mother" и т.д.
Тут правильным ответом должно быть "abba com mother" (частота — 3 раза).
"""

import unittest


def mostly_count(source):
    words = source.split()

    counts = {}

    for i in range(len(words) - 2):
        triplet = ' '.join(words[i:i + 3])
        counts.setdefault(triplet, 0)
        counts[triplet] += 1

    max_count = 0
    result = None

    for key, value in counts.items():
        if value > max_count:
            max_count = value
            result = key

    return result


class TestMostlyCount(unittest.TestCase):
    def test_abba_mother(self):
        test_string = 'abba com mother bill mother com abba dog abba mother com'

        expected = 'abba com mother'

        self.assertEqual(mostly_count(test_string), expected)
