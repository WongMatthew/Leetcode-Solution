# beats 20% runtime and 80% memory

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        if len(nums)==1:
            return 1
        x=nums[0]
        i=0
        while i<len(nums)-1:
            if x==nums[1+i]:
                del nums[1+i]
            else:
                x=nums[1+i]
                i+=1
        return i+1