from unittest import TestCase

from RomanToInteger.solution import Solution


class TestDict(TestCase):
    def test_what_order_are_keys(self):
        # do keys come out of the dictionary the same order I put them in there?
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.assertEqual(list(roman_numerals.keys()), ['I', 'V', 'X', 'L', 'C', 'D', 'M'])

class TestSolution(TestCase):
    def test_individual_numerals(self):
        known = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = Solution()
        for numeral in known:
            self.assertEqual(s.romanToInt(numeral), known[numeral])

    def test_multiple_numerals(self):
        s = Solution()
        self.assertEqual(s.romanToInt('II'), 2)
        self.assertEqual(s.romanToInt('DCXXI'), 621)

    def test_descending_order(self):
        s = Solution()
        self.assertEqual(s.romanToInt('MDC'), 1600)
        self.assertEqual(s.romanToInt('LX'), 60)
        self.assertEqual(s.romanToInt('VIII'), 8)

    def test_subtractive_notation(self):
        s = Solution()
        known = {
            'IV': 4,
            'IX': 9,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        for numeral in known:
            self.assertEqual(s.romanToInt(numeral), known[numeral])

    def test_max_value(self):
        s = Solution()
        self.assertEqual(s.romanToInt('MMMCMXCIX'), 3999)
