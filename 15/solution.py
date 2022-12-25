# beats 90% runtime and 48% memory

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        result = []
        
        #loop through nums ~ keep track on index and num
        for i, num in enumerate(nums):
            l = i +1
            r = len(nums) -1

            # skip duplicates
            if i > 0 and nums[i - 1] == num:
                continue

            # break if l and r cross
            while l < r:
                s = num + nums[l] + nums[r]
            # move left and right pointers inward based on +/- of 's' b/c nums is sorted
                if s == 0:
                    result.append([num, nums[l], nums[r]])
                    # skip duplicates on left and right
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l +=1
                    r -=1
                
                elif s<0:
                    l+=1
                else:
                    r-=1
        return result