# beats 87% runtime and 63% memory

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # set up permutation stack and results list
        perm, res = [], []
        # set up keys for dictionary
        count = {n:0 for n in nums}

        # add values to dictionary
        for n in nums:
            count[n] += 1

        # depth first search
        def dfs():
            # break out when finished
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