class Solution:
    def reverse(self, x):
        negate = (True if str(x)[0] == '-' else False)
        r = 0
        if negate:
            y = str(x)
            y = y[1:]
            r = int(str(y)[::-1]) * -1
        else:
            r = int(str(x)[::-1])

        overflow = False
        if r >= (2**31) or r <= -2**31:
            overflow = True
        if overflow:
            return 0
        return r
