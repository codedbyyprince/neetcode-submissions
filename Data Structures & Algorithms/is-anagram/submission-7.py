class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for i in s:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        for i in t:
            if i not in hmap:
                return False
            else:
                hmap[i] -= 1
        if all(v == 0 for v in hmap.values()):
            return True
        else:
            return False