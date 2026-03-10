# Leetcode Link: https://leetcode.com/problems/palindrome-linked-list/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given the head of a singly linked list, return true if it is a palindrome.
# Example: [1,2,2,1] -> True
# ---------- Approach ----------
# 1) Find middle (slow/fast pointers)
# 2) Reverse second half
# 3) Compare first and reversed second half
# Time: O(n) | Space: O(1)
class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # Compare both halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
