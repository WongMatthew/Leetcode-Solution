# beats 97% of runtime and 63% of memory

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        result = 0
        max_diff = 10001
        
        # base case --> if 3x nums in list
        if len(nums) == 3:
            return sum(nums)

        #loop through nums ~ keep track on index and num
        for i, num in enumerate(nums):
            l = i +1
            r = len(nums) -1

            # break if l and r cross
            while l < r:
                s = num + nums[l] + nums[r]

                diff = abs(s - target)

                if diff < max_diff:
                    max_diff = diff
                    result = s
                
                elif s<target:
                    l+=1
                elif s>target:
                    r-=1
                # base case -> if target is sum
                else:
                    return s
        return result