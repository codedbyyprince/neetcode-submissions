class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1 ):
            t = arr[i] 
            max_of_rest = max(arr[i+1:])
            arr[i] = max_of_rest
            
        arr[-1] = -1
        return arr