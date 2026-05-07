class Solution:
    def scoreOfString(self, s: str) -> int:
        nums = []
        for i in range(len(s)):
            nums.append(ord(s[i]))
        
        total = 0
        for i in range(len(nums) - 1):   # stop before last element
            total += abs(nums[i] - nums[i+1])
        
        return total