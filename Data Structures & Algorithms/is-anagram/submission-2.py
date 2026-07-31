class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}

        for char in s:
            seen1[char] = seen1.get(char, 0) + 1
        for char in t:
            seen2[char] = seen2.get(char, 0) + 1
        
        return seen1 == seen2