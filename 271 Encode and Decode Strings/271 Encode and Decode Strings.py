# Leetcode Link: https://leetcode.com/problems/encode-and-decode-strings/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design encode and decode methods for a list of strings.
# Example: ["hello","world"] -> encode -> "5#hello5#world" -> decode -> ["hello","world"]
# ---------- Approach ----------
# Prefix each string with its length and a delimiter '#'. Decode by reading length, then extracting.
# Time: O(n) for both encode and decode | Space: O(n)
class Codec:
    def encode(self, strs) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str):
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result
