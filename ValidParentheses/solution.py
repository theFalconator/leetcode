from collections import deque


class Solution:
    def isValid(self, s):
        '''
        Determine if parentheses are balanced in a given string.
        :param s: string containing parentheses / brackets.
        :return: True if parentheses are balanced, otherwise False.
        '''
        matching = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        buffer = deque()

        # populate double ended queue with parens
        for paren in s:
            buffer.append(paren)

        # cannot be balanced if there are an odd number of parens in it
        if len(buffer) % 2 != 0:
            return False
        else:
            while len(buffer) > 0:
                try:
                    front = buffer.popleft()
                    back = buffer.pop()
                    if back != matching[front]:
                        return False
                except KeyError:
                    # only have opening parens as keys
                    # if there is a closing paren first, this will throw a key error
                    # matching implies that we have open first -- return false
                    return False

        return True
