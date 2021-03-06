from unittest import TestCase
from TwoSum.solution import Solution


class TestSolution(TestCase):
    def test_twoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[3, 2, 4], target=6), [1, 2])
        self.assertEqual(s.twoSum(nums=[2, 7, 11, 15], target=9), [0, 1])

    def test_empty_input(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[], target=5), None)

    def test_repeated_input(self):
        s = Solution()
        self.assertEqual(s.twoSum(nums=[3, 3], target=6), [0, 1])
