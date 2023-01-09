# beats 91% runtime and 82% memory

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif i < len(nums)-1 and target < nums[i+1]:
                return i+1
        return len(nums)