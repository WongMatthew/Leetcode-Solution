# beat 81% runtime and 56% memory usage

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        # base case
        if sum(nums) == target and len(nums) == 4:
            ans.append(nums)
            return ans
        
        # set up initial pointers w/ i and j 
        # points to beginning of list
        for i in range(len(nums)):
            # check for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                # check for duplicates
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                # initialize vars
                l, r = j+1, len(nums)-1
                
                # 3sum code
                while l <r:
                    s= nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                    elif s <target:
                        l +=1
                    else:
                        r -= 1
        return ans