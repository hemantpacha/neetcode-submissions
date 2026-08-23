class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        tot_max = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                tot_max = max(tot_max, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return tot_max