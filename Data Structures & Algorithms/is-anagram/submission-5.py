class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen1 = {}
        for c in s:
            seen1[c] = seen1.get(c, 0) + 1
        
        seen2 = {}
        for c in t:
            seen2[c] = seen2.get(c, 0) + 1
        
        for c in seen1:
            if seen1.get(c, 0) != seen2.get(c, 0):
                return False
        
        return True