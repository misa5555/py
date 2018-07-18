class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            mid = (total_len // 2 - 1, total_len // 2)
        else:
            mid = (total_len // 2, total_len // 2)


