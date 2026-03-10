# Leetcode Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given triplets and target triplet, determine if you can merge (take element-wise max)
# some triplets to form the target.
# Example: triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5] -> True
# ---------- Approach ----------
# Greedy: a triplet is usable only if none of its values exceed the target.
# Among usable triplets, check if each target position is achievable.
# Time: O(n) | Space: O(1)
class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        good = set()
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    if t[i] == target[i]:
                        good.add(i)
        return len(good) == 3
