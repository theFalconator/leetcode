class Solution:
    def romanToInt(self, s):
        '''
        Converts roman numeral string to integer.
        :param s: Input string should be a roman numeral ranging from 1 to 3999.
        :return: An integer representation of the input.
        '''
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        numerals = list(roman_numerals.keys())

        if len(s) == 1:
            return roman_numerals.get(s, None)
        else:
            total = 0
            for i in range(0, len(s)):
                # Roman numerals are always written from left to right in order of value.
                if i < len(s) - 1:
                    # look ahead to see if we need to add or subtract
                    current = s[i]
                    next = s[i + 1]
                    if numerals.index(current) < numerals.index(next):
                        total -= roman_numerals.get(s[i], 0)
                    else:
                        total += roman_numerals.get(s[i], 0)
                else:
                    total += roman_numerals.get(s[i], 0)
            return total
