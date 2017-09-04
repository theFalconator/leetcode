from unittest import TestCase

from RemoveElement.solution import Solution


class TestSolution(TestCase):
    def test_empty_list(self):
        s = Solution()
        self.assertEqual(s.removeElement([], 1), 0)

    def test_single_element(self):
        s = Solution()
        self.assertEqual(s.removeElement([2], 3), 1)

    def test_sample_input(self):
        s = Solution()
        self.assertEqual(s.removeElement([3, 2, 2, 3], 3), 2)

    def test_repeated_input(self):
        s = Solution()
        self.assertEqual(s.removeElement([1, 1, 1], 1), 0)
