import math

class Solution:
    def splitInt(self, x):
        l = []
        while x % 10 != 0:
            l.append(x % 10)
            x = math.floor(x/10)
        return l

    def isPalindrome(self, x):
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        else:
            l = self.splitInt(x)
            first_half = l[0:math.floor(len(l)/2)]
            second_half = l[math.floor(len(l)/2):len(l)]
            if first_half[::-1] == second_half:
                return True
            return False