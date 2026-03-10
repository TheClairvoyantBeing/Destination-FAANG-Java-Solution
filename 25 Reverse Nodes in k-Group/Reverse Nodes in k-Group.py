# Leetcode Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list. If the number of nodes is not a multiple of k,
# the remaining nodes at the end should stay as-is.
#
# Example:
#   Input: head = [1,2,3,4,5], k = 2
#   Output: [2,1,4,3,5]

# ---------- Approach ----------
# Recursive approach — count k nodes; if there are k nodes, reverse them and
# recursively process the remaining list.
#
# Time Complexity : O(n) — each node is visited twice (count + reverse)
# Space Complexity: O(n/k) — recursion depth

class Solution:
    def reverseKGroup(self, head, k: int):
        # Count if there are at least k nodes remaining
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1

        if count < k:
            return head  # Not enough nodes — return as-is

        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # head is now the tail of the reversed segment; connect to next group
        head.next = self.reverseKGroup(curr, k)
        return prev  # prev is the new head of this reversed segment
