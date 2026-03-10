# Leetcode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the head of a linked list, remove the n-th node from the end of the list
# and return its head.
#
# Example:
#   Input: head = [1,2,3,4,5], n = 2
#   Output: [1,2,3,5]  (removed node 4)

# ---------- Approach ----------
# Two-pointer gap technique — advance the right pointer n steps ahead, then move
# both pointers until right reaches the end. Left pointer will be just before
# the node to remove.
#
# Time Complexity : O(L) — where L is the length of the list (single pass)
# Space Complexity: O(1)

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)  # Dummy node handles edge case of removing head
        left = dummy
        right = head

        # Create a gap of n nodes between left and right
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Skip the target node
        left.next = left.next.next
        return dummy.next
