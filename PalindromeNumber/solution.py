import math


class Solution:
    def splitInt(self, x):
        l = []
        while x % 10 != 0:
            l.append(x % 10)
            x = math.floor(x / 10)
        return l

    def isPalindrome(self, x):
        # negative numbers cannot be palindromes
        if x < 0:
            return False

        # single digit numbers can.
        if x > 0 and x < 10:
            return True

        # numbers ending in zero cannot.
        if x % 10 == 0 and x != 0:
            return False
        else:
            l = self.splitInt(x)

            # even number of digits
            if len(l) % 2 == 0:
                i = math.floor(len(l) / 2)
                j = math.floor(len(l) / 2)
                first_half = l[0:i]
                second_half = l[j:len(l)]
                if first_half[::-1] == second_half:
                    return True
                return False

            # odd number of digits
            else:
                i = math.floor(len(l) / 2)

                first_half = l[0:i]
                second_half = l[i + 1:len(l)]
                if first_half[::-1] == second_half:
                    return True
                return False
