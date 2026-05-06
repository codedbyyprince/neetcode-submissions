from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        new = set(nums)
        if len(new) == len(nums):
            return False
        else:
            return True
