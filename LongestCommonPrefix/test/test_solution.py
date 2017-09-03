from unittest import TestCase

from LongestCommonPrefix.solution import Solution


class TestSolution(TestCase):
    def test_words_with_suffixes(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(['child', 'childish']), 'child')
        self.assertEqual(s.longestCommonPrefix(['work', 'worker']), 'work')
        self.assertEqual(s.longestCommonPrefix(['like', 'likeable']), 'like')

    def test_no_common_prefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(['leetcode', 'monkey']), '')

    def test_empty_input(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix([]), '')

    def test_sample_input(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(['leets', 'leetcode', 'leet', 'leeds']), 'lee')
