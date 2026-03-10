# Leetcode Link: https://leetcode.com/problems/middle-of-the-linked-list/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given head of linked list, return the middle node. If two middle nodes, return second.
# Example: [1,2,3,4,5] -> [3,4,5]
# ---------- Approach ----------
# Slow & fast pointers: when fast reaches end, slow is at middle.
# Time: O(n) | Space: O(1)
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
