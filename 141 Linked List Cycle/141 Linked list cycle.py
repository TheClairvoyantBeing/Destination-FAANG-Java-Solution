# Leetcode Link: https://leetcode.com/problems/linked-list-cycle/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given head of a linked list, determine if it has a cycle.
# ---------- Approach ----------
# Floyd's Cycle Detection (tortoise and hare): slow moves 1 step, fast moves 2 steps.
# If they meet, there's a cycle.
# Time: O(n) | Space: O(1)
class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False  # Fast reached the end — no cycle
            slow = slow.next
            fast = fast.next.next
        return True  # Slow and fast met — cycle exists
