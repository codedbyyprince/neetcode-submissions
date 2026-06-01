class Solution:
    def minimumDifference(self, nums: List[int], k: int):
        l = 0 
        r = k - 1
        res = float('inf')
        nums.sort()
        while r < len(nums):
            res = min(res , nums[r] - nums[l])
            l += 1
            r += 1
        
        return res
