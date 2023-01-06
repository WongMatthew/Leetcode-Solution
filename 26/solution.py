# beats 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=nums[0]
        i=0
        while i<len(nums)-1:
            if x==nums[1+i]:
                del nums[1+i]
            else:
                x=nums[1+i]
                i+=1
        return i+1