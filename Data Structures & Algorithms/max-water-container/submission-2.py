class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        find the max subarray
        start with a left pointer and right pointer for each subarray
        take the max
        """

        left = 0
        right = len(heights) - 1
        temp_max = 0
        final_max = 0
        for i in range(len(heights)):
            while left < right:
                temp_max = min(heights[left], heights[right]) * (right - left)
                final_max = max(final_max, temp_max)
                if heights[left] < heights[right]:
                    left += 1
                elif heights[right] < heights[left]:
                    right -= 1
                else:
                    left += 1
                    right -= 1
                
        return final_max
            