
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and idx < n:
                nums1[i] = nums2[idx]
                idx += 1
        nums1.sort()
