# beats 95% runtime and 49% memory

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

            # Iterate through the array of numbers
        for index in range(0, len(nums)):
            # Calculate the difference between the target and the current element
            diff = target - nums[index]
            
            # Check if the difference is already in the hash map
            if hash_map.get(diff) == None:
                # If not, add the current element and its index to the hash map
                hash_map[nums[index]] = index
                
            else:
                # If it is, return the indices of the current element and the element in the hash map
                # that add up to the target
                return [index, hash_map[diff]]