# Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an unsorted array of integers, return the length of the longest consecutive
# elements sequence. Must run in O(n) time.
# Example: nums=[100,4,200,1,3,2] -> 4 (sequence: [1,2,3,4])
# ---------- Approach ----------
# HashSet — for each number that is the START of a sequence (num-1 not in set),
# count consecutive numbers. This ensures each element is processed at most twice.
# Time: O(n) | Space: O(n)
class Solution:
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:  # Only start counting from sequence start
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest = max(longest, current_streak)
        return longest
