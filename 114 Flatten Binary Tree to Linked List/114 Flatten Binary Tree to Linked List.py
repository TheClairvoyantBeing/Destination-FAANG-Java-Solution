# Leetcode Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given root of a binary tree, flatten it to a linked list in-place using right pointers
# in pre-order traversal order. Example: [1,2,5,3,4,null,6] -> [1,null,2,null,3,null,4,null,5,null,6]
# ---------- Approach ----------
# Morris Traversal style: for each node with a left child, find the rightmost node of the
# left subtree and connect it to the right child. Then move left subtree to the right.
# Time: O(n) | Space: O(1)
class Solution:
    def flatten(self, root) -> None:
        curr = root
        while curr:
            if curr.left:
                rightmost = curr.left          # Find rightmost of left subtree
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = curr.right   # Connect to right child
                curr.right = curr.left         # Move left subtree to right
                curr.left = None               # Clear left pointer
            curr = curr.right                  # Move to next node
