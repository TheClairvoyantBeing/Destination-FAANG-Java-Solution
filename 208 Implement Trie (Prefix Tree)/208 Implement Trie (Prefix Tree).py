# Leetcode Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Implement a Trie with insert, search, and startsWith methods.
# ---------- Approach ----------
# Tree of dictionaries. Each node is a dict of children. Use a special '#' key to mark end of word.
# Time: O(m) for all ops (m = word/prefix length) | Space: O(total characters stored)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end
    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
    def _find_node(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
