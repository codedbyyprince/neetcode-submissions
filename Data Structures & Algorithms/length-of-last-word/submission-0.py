class Solution:
    def lengthOfLastWord(self, s: str):
        words = s.split()

        return len(words[-1])