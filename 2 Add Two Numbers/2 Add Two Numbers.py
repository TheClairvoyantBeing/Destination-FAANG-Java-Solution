# Leetcode Link: https://leetcode.com/problems/add-two-numbers/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# Example:
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [7,0,8]
#   Explanation: 342 + 465 = 807

# ---------- Approach ----------
# Traverse both linked lists simultaneously, adding corresponding digits along with
# any carry from the previous addition. Create new nodes with the resulting digit.
#
# Time Complexity : O(max(m, n)) — where m and n are the lengths of the two lists
# Space Complexity: O(max(m, n)) — for the new linked list

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # Sentinel node to simplify list construction
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0        # Get digit from l1, or 0 if exhausted
            val2 = l2.val if l2 else 0        # Get digit from l2, or 0 if exhausted
            total = val1 + val2 + carry       # Sum digits + carry
            carry = total // 10               # Carry for next position
            curr.next = ListNode(total % 10)  # Create node with ones digit
            curr = curr.next                  # Advance pointer
            l1 = l1.next if l1 else None      # Move to next node if available
            l2 = l2.next if l2 else None

        return dummy.next  # Skip sentinel and return result list
