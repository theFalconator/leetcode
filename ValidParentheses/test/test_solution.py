from unittest import TestCase

from ValidParentheses.solution import Solution


class TestSolution(TestCase):
    def test_simple_pairs(self):
        s = Solution()
        self.assertEqual(s.isValid('()'), True)
        self.assertEqual(s.isValid('[]'), True)
        self.assertEqual(s.isValid('{}'), True)

    def test_correct_nested_pairs(self):
        s = Solution()
        self.assertEqual(s.isValid('([{}])'), True)
        self.assertEqual(s.isValid('([])'), True)

    def test_mismatched_pairs(self):
        s = Solution()
        self.assertEqual(s.isValid('{)'), False)
        self.assertEqual(s.isValid('[)'), False)

    def test_closing_first(self):
        s = Solution()
        self.assertEqual(s.isValid('}()'), False)

    def test_odd_number_of_parens(self):
        s = Solution()
        self.assertEqual(s.isValid('('), False)

    def test_sample_input(self):
        s = Solution()
        self.assertEqual(s.isValid('()[]{}'), True)
