class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #loop from left to right
        l = 0
        r = 0
        mostFreq = 0
        maxWindow = 0
        count = {}
        
        while r < len(s):
            #Get the most freq char in window
            count[s[r]] = count.get(s[r], 0) + 1
            mostFreq = max(mostFreq, count[s[r]])

            #window size contains more subsitutions than allowed
            while (r - l + 1) - mostFreq > k:
                count[s[l]] -= 1
                l += 1

            maxWindow = max(maxWindow, r - l + 1)
            r += 1
        
        return maxWindow
