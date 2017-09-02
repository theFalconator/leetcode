from unittest import TestCase
from ReverseInteger.solution import Solution

class TestSolution(TestCase):
    def test_reverse(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)

    def test_negative(self):
        s = Solution()
        self.assertEqual(s.reverse(-123), -321)

    def test_overflow(self):
        s = Solution()
        self.assertEqual(s.reverse(1534236469), 0)
        self.assertEqual(s.reverse(1563847412), 0)
        self.assertEqual(s.reverse(-2147483648), 0)
