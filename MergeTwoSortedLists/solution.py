class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __repr__(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(str(current.val))
            current = current.next

        return '-->'.join(nodes)


class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        Takes two sorted linked lists and merges them returning the merged list.
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
