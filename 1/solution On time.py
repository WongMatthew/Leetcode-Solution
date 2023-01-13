class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index in range(0, len(nums)):
            diff = target - nums[index]
            if hash_map.get(diff) == None:
                hash_map[nums[index]] = index
            else:
                return [index, hash_map[diff]]