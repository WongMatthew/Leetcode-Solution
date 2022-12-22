class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # step 1 and step 2: combine and sort arrays
        combined = sorted(nums1 + nums2)
        # step 3: check if even or odd # of values
        if len(combined) % 2 == 1: 
            print(len(combined) // 2)
            return combined[len(combined) // 2]
        else:
            ans = float((combined[len(combined) // 2] + combined[len(combined) // 2 - 1]))
            return ans / 2