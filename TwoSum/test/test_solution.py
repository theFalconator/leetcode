from unittest import TestCase
from TwoSum.solution import Solution


class TestSolution(TestCase):
    def test_twoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[3, 2, 4], target=6), [1, 2])

    def test_empty_input(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[], target=5), None)

    def test_duplicate_input(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[3, 3], target=6), [0, 1])
