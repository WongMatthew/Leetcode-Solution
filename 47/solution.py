# beats 87% runtime and 63% memory

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm, res = [], []
        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    perm.append(n)
                    dfs()
                    perm.pop()
                    count[n] += 1

        dfs()
        return res