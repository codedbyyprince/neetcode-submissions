class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int):
        count = 0 
        l =  0 
        r = k - 1

        while r < len(arr):
            sub = arr[l:r+1]
            avg = sum(sub) / len(sub)
            if avg >= threshold:
                count += 1
            l += 1
            r += 1
        return count