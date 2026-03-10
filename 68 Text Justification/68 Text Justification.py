# Leetcode Link: https://leetcode.com/problems/text-justification/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of words and a width maxWidth, format the text such that each line
# has exactly maxWidth characters and is fully (left and right) justified.
# The last line should be left-justified.
#
# Example:
#   Input: words = ["This","is","an","example","of","text","justification."], maxWidth = 16
#   Output: ["This    is    an", "example  of text", "justification.  "]

# ---------- Approach ----------
# Greedy — pack as many words as possible into each line. Distribute extra spaces
# evenly between words (round-robin). Last line is left-justified.
#
# Time Complexity : O(n) — where n is total number of characters in all words
# Space Complexity: O(maxWidth) — for building each line

class Solution:
    def fullJustify(self, words, maxWidth: int):
        result = []
        line = []
        line_length = 0  # Total character count of words in current line

        for word in words:
            # Check if adding this word would exceed maxWidth
            # line_length + len(word) + len(line) accounts for minimum 1 space between words
            if line_length + len(word) + len(line) > maxWidth:
                # Distribute extra spaces across the line
                for i in range(maxWidth - line_length):
                    # Round-robin: distribute extra spaces starting from the left
                    line[i % (len(line) - 1 or 1)] += ' '
                result.append(''.join(line))
                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        # Last line: left-justified, padded with spaces on the right
        result.append(' '.join(line).ljust(maxWidth))
        return result
