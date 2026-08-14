from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq hashmap num : freq
        seen = {}

        for num in nums:
            seen[num] = seen.get(0, num) + 1

        - rearrange seen from highest val to lowest

        sort seen

        for i in range()

        """
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

