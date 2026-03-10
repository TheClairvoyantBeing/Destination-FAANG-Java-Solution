# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/sort-list/
# Video Solution: https://www.youtube.com/watch?v=7halZ77R55o
# **************** Python Solution ***********************
# ---------- Question ----------
# Sort a linked list in O(n log n) time and O(1) memory (ignoring recursion stack).
# ---------- Approach ----------
# Merge Sort on linked list: find middle, split, sort halves recursively, merge.
# Time: O(n log n) | Space: O(log n) recursion stack
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    def getMid(self, head):
        prev = None
        while head and head.next:
            prev = head if prev is None else prev.next
            head = head.next.next
        mid = prev.next
        prev.next = None  # Split the list
        return mid
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1; l1 = l1.next
            else:
                tail.next = l2; l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
