# beats 99% runtime and 93.24% memory

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # base case if nums is empty
        if len(nums) == 0: 
            return [-1,-1]

        temp = []

        # find index of each target
        for i in range(len(nums)):
            if nums[i] == target: 
                temp.append(i)

        # check if theres anything inside of temp 
        if len(temp) == 0: 
            return [-1, -1]
        # return first and last indices of target
        else: 
            return [temp[0],temp[-1]]