# beats 87.64% runtime and 91% memory

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize `k` to keep track of the position in `nums` where the next non-`val` element should be placed
        k = 0
        # Loop through the elements in `nums`
        for i in range(len(nums)):
            # If current element is `val`, skip
            if nums[i] == val:
                continue
            # else, place the current element at position `k` and increment `k`
            nums[k] = nums[i]
            k += 1
        # Return the new length of `nums` after removing all occurrences of `val`
        return k