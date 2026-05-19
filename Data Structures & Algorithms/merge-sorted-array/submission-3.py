class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new = []
        arr1 = nums1[:m]
        
        new = arr1 + nums2
        new.sort()
        nums1[:] = new
        return nums1