# Leetcode Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# **************** Python Solution ***********************
# ---------- Question ----------
# Find the k-th largest element in an unsorted array. Not the k-th distinct element.
# Example: nums=[3,2,1,5,6,4], k=2 -> 5
# ---------- Approach ----------
# Min-heap of size k: push all elements, pop when size exceeds k. Top of heap = k-th largest.
# Time: O(n log k) | Space: O(k)
import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)  # Remove smallest, keep k largest
        return heap[0]  # Top = k-th largest
