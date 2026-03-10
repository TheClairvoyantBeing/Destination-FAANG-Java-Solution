# Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array and integer k, return the k most frequent elements.
# Example: nums=[1,1,1,2,2,3], k=2 -> [1,2]
# ---------- Approach ----------
# Bucket Sort: index = frequency, value = list of numbers with that frequency.
# Collect from highest frequency bucket first.
# Time: O(n) | Space: O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
