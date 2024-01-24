class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = nums1 + nums2
        merge.sort()
        mergeSize = len(merge)

        if (mergeSize % 2 == 0):
            return float(merge[int(mergeSize / 2) - 1] + merge[int(mergeSize / 2)]) / 2
        else:
            return merge[int(mergeSize / 2)]
