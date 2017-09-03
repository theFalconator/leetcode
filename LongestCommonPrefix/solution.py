class Solution:
    def longestCommonPrefix(self, strs):
        '''
        Given a list of strings return the longest common prefix.
        :param strs: List of strings to search for prefix
        :return: string containing the longest common prefix
        '''
        if not strs:
            return ''

        prefix = strs[0]
        for i in range(0, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix
