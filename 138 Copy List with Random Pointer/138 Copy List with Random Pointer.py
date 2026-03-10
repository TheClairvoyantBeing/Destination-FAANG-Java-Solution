# Leetcode Link: https://leetcode.com/problems/copy-list-with-random-pointer/
# **************** Python Solution ***********************
# ---------- Question ----------
# Deep copy a linked list where each node has a next pointer and a random pointer.
# ---------- Approach ----------
# Two-pass with hash map: first pass creates clones, second pass sets next and random pointers.
# Time: O(n) | Space: O(n)
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:                                # First pass: create all clones
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:                                # Second pass: set pointers
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]
