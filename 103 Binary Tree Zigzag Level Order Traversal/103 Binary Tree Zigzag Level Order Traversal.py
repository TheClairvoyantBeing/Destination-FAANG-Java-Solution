# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Video Solution: https://www.youtube.com/watch?v=Oy3g4SEKNw0

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the root of a binary tree, return the zigzag level order traversal of its values
# (i.e., from left to right, then right to left for the next level and alternate).
#
# Example:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[3],[20,9],[15,7]]

# ---------- Approach ----------
# BFS with a deque — use a null delimiter to separate levels. Alternate the direction
# of insertion (addLast vs addFirst) at each level using a boolean flag.
#
# Time Complexity : O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        results = []
        node_queue = deque([root, None])  # None acts as level delimiter
        level_list = deque()
        is_order_left = True

        while node_queue:
            curr_node = node_queue.popleft()
            if curr_node is not None:
                if is_order_left:
                    level_list.append(curr_node.val)      # Left-to-right
                else:
                    level_list.appendleft(curr_node.val)  # Right-to-left

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # End of current level
                results.append(list(level_list))
                level_list = deque()
                if node_queue:
                    node_queue.append(None)  # Add delimiter for next level
                is_order_left = not is_order_left  # Toggle direction

        return results
