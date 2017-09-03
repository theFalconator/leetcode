class Solution:
    def isValid(self, s):
        '''
        Determine if parentheses are balanced in a given string.
        :param s: string containing parentheses / brackets.
        :return: True if parentheses are balanced, otherwise False.
        '''
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        buffer = []

        # populate double ended queue with parens
        for paren in s:
            if paren in matching.values():
                buffer.append(paren)
            elif paren in matching.keys():
                try:
                    if not buffer:
                        return False
                    if matching[paren] != buffer.pop():
                        return False
                except KeyError:
                    return False
            else:
                return False

        return buffer == []
