class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return None

        attempts = set()
        attempts.add(nums[0])

        for i in range(1, len(nums)):
            first = nums[i]
            needed = target - first
            if needed in attempts:
                return [nums.index(needed), nums.index(first)]
            else:
                attempts.add(first)

        return None
