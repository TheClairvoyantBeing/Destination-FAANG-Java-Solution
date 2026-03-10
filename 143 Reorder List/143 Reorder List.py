# LeetCode Link: https://leetcode.com/problems/reorder-list/
# Youtube Explaination: https://youtu.be/lBdS4AV1EGw
# **************** Python Solution ***********************
# ---------- Question ----------
# Reorder list from L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→L2→Ln-2→...
# Example: [1,2,3,4] -> [1,4,2,3]
# ---------- Approach ----------
# Three steps: 1) Find middle 2) Reverse second half 3) Merge alternately
# Time: O(n) | Space: O(1)
class Solution:
    def reorderList(self, head) -> None:
        if not head:
            return
        # Step 1: Find the middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2: Reverse the second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Step 3: Merge two halves alternately
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp
