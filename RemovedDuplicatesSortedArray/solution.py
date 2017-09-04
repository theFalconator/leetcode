class Solution:
    def removeDuplicates(self, nums):
        '''
        Returns the length of the sorted list with duplicates removed.
        :param nums: sorted list of integers
        :return: length of the list with duplicates removed
        '''

        # Empty list should return a length of zero
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
