# Leetcode Link: https://leetcode.com/problems/hand-of-straights/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given hand of cards, rearrange into groups of groupSize consecutive cards.
# Example: hand=[1,2,3,6,2,3,4,7,8], groupSize=3 -> True ([1,2,3],[2,3,4],[6,7,8])
# ---------- Approach ----------
# Greedy: sort, for each card with remaining count > 0, try to form a group starting from it.
# Time: O(n log n) | Space: O(n)
from collections import Counter
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]
                for i in range(card, card + groupSize):
                    if count[i] < freq: return False
                    count[i] -= freq
        return True
