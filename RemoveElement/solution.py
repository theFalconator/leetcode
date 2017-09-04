class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                i = 0
            else:
                i += 1

        return len(nums)
