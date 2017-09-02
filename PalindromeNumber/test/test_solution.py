from unittest import TestCase
from PalindromeNumber.solution import Solution


class TestSolution(TestCase):
    def test_splitNumber(self):
        s = Solution()
        self.assertEqual(s.splitInt(1221), [1, 2, 2, 1])
        self.assertEqual(s.splitInt(150), [])

    def test_isPalindrome(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(1221), True)
        self.assertEqual(s.isPalindrome(150), False)
