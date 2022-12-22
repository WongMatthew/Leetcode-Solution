class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()
        pair = []
        i = 0
        foundPair = False
        
        while i < len(nums):
            table[nums[i]] = i
            i +=1

        i = 0 
    
        while i < len(nums) and not foundPair:
            remainder = target - nums[i]
            
            if remainder in table:
                if i != table[remainder]:
                    pair.append(i)
                    pair.append(table[remainder])
                    foundPair = True
        
            i +=1
    
        return pair