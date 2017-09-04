class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


def connect_nodes(lst):
    prev = lst[0]
    for node in lst[1:]:
        prev.next = node
        prev = node
    return lst[0]


class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        Takes two sorted linked lists and merges them returning the merged list.
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            min_node = l1
            min_node.next = self.mergeTwoLists(l1.next, l2)
        elif l1.val > l2.val:
            min_node = l2
            min_node.next = self.mergeTwoLists(l1, l2.next)
        return min_node
