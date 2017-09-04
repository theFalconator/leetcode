from unittest import TestCase

from MergeTwoSortedLists.solution import ListNode, Solution


class TestSolution(TestCase):
    def test_two_empty_lists(self):
        s = Solution()
        self.assertEqual(s.mergeTwoLists(None, None), None)

    def test_one_list_empty(self):
        s = Solution()
        self.assertEqual(s.mergeTwoLists(None, ListNode(1)), ListNode(1))
        self.assertEqual(s.mergeTwoLists(ListNode(1), None), ListNode(1))

    def test_insert_at_front(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = ListNode(2)
        l2.next = ListNode(3)

        merged = ListNode(1)
        merged.next = ListNode(2)
        merged.next.next = ListNode(3)
        self.assertEqual(s.mergeTwoLists(l1, l2), merged)
