# Leetcode Link: https://leetcode.com/problems/reverse-linked-list/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given the head of a singly linked list, reverse it and return the reversed list.
# Example: [1,2,3,4,5] -> [5,4,3,2,1]
# ---------- Approach ----------
# Iterative: maintain prev and curr pointers. At each step, reverse the link direction.
# Time: O(n) | Space: O(1)
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next    # Save next node
            curr.next = prev    # Reverse the link
            prev = curr         # Move prev forward
            curr = temp         # Move curr forward
        return prev             # New head
