# Leetcode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a data structure: addWord(word) adds a word, search(word) searches with '.'
# matching any single character. Example: search("b.d") matches "bad", "bed"
# ---------- Approach ----------
# Trie + DFS for wildcard matching. When '.' is encountered, try all children.
# Time: O(m) for add, O(26^m) worst-case for search with wildcards | Space: O(total chars)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i + 1)
        return dfs(self.root, 0)
