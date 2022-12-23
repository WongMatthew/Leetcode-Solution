# beats 98% of runtime and 53% of memory 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        length = len(height)
        low = 0
        high = length-1

        while(low < high):
            # max(max_area, (high - low) * min(height[low], height[high])) --> get new max area ~ comparing current max_area and new max_area
            # min(height[low], height[high]) --> compare values at each end of the list
            max_area = max(max_area, (high - low) * min(height[low], height[high]))
            # move pointers based on which side has the smaller height
            if height[low] < height[high]:
                low+=1
            else:
                high-=1 

        return max_area