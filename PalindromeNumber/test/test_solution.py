from unittest import TestCase

from PalindromeNumber.solution import Solution


class TestSplit(TestCase):
    def test_even_number_of_digits(self):
        s = Solution()
        self.assertEqual(s.splitInt(1221), [1, 2, 2, 1])

    def test_ends_in_zero(self):
        s = Solution()
        self.assertEqual(s.splitInt(150), [1, 5, 0])

    def test_odd_number_of_digits(self):
        s = Solution()
        self.assertEqual(s.splitInt(121), [1, 2, 1])

    def test_intersperced_zeros(self):
        s = Solution()
        self.assertEqual(s.splitInt(1000030001), [1, 0, 0, 0, 0, 3, 0, 0, 0, 1])


class TestPalindrome(TestCase):
    def test_ends_in_zero(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(150), False)

    def test_negative_number(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(-5), False)

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(0), True)

    def test_odd_number_of_digits(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(121), True)

    def test_even_number_of_digits(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(1221), True)

    def test_intersperced_zeros(self):
        s = Solution()
        self.assertEqual(s.isPalindrome(1000030001), False)
