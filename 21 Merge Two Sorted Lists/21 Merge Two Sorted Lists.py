# Leetcode Link: https://leetcode.com/problems/merge-two-sorted-lists/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list and return the head.
#
# Example:
#   Input: list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]

# ---------- Approach ----------
# Use a dummy head and a tail pointer. Compare the current nodes of both lists,
# append the smaller one, and advance that list's pointer.
#
# Time Complexity : O(m + n)
# Space Complexity: O(1) — reusing existing nodes

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Sentinel node
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes
        tail.next = list1 if list1 else list2
        return dummy.next
