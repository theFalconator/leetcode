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
            firstHalf = l[0:math.floor(len(l)/2)]
            secondHalf = l[math.floor(len(l)/2):len(l)]
            if firstHalf[::-1] == secondHalf:
                return True
            return False