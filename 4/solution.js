/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // step 1 and step 2
    const combined = [... nums1, ... nums2].sort()
    // step 3
    if (combined.length % 2 === 1)
        return combined[Math.floor(combined.length/2)] 
    else
        return (
            combined[Math.floor(combined.length/2)] + (combined[Math.floor(combined.length/2)-1]))/2
    }