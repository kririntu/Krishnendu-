class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        snums1 = sorted(nums1)
        snums2 = sorted(nums2)
        tnum = sorted(list(snums1 + snums2))
        n = len(tnum)
        if n == 0:
            raise ValueError("Median not defined for an empty sequence")
        if n % 2 == 1:
        # Odd case: return the middle element
            median = tnum[n // 2]
        else:
        # Even case: average the two middle elements
            mid1 = tnum[n // 2 - 1]
            mid2 = tnum[n // 2]
            median = (mid1 + mid2) / 2.0
        
        return median
        
        