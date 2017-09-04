from unittest import TestCase

from RemovedDuplicatesSortedArray.solution import Solution


class TestSolution(TestCase):
    def test_empty_list(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([]), 0)

    def test_sample_input(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(s.removeDuplicates([1, 1, 2, 3, 4]), 4)

    def test_repeats(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1, 1, 1]), 1)

    def test_no_duplicates(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1, 2, 3]), 3)
