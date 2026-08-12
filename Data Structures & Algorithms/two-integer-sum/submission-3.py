class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        counter = 0
        for num in nums:
            if target - num in seen:
                return [seen[target - num], counter]
            seen[num] = counter
            counter += 1
