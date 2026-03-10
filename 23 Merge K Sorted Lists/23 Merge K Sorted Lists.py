# Leetcode Link: https://leetcode.com/problems/merge-k-sorted-lists/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given an array of k linked-lists, each sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example:
#   Input: lists = [[1,4,5],[1,3,4],[2,6]]
#   Output: [1,1,2,3,4,4,5,6]

# ---------- Approach ----------
# Min-Heap — push the head of each list into a heap. Pop the smallest,
# add it to the result, and push its next node into the heap.
# The index 'i' is used as a tiebreaker to avoid comparing ListNode objects.
#
# Time Complexity : O(N log k) — N total nodes, k lists
# Space Complexity: O(k) — heap size

import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))  # (value, tiebreaker, node)

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
