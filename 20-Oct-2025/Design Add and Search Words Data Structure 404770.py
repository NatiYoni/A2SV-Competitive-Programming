# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class  TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for l in word:
            ch = ord(l) - 97

            if not cur.children[ch]:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(node,i):
            if not node:
                return False
            if i == len(word) and node.end:
                return True

            ans = False
            if i < len(word) and word[i] == ".":
                for j in range(26):
                    ans |= dfs(node.children[j], i+1)
            elif i < len(word):
                ch = ord(word[i]) - 97
                ans |= dfs(node.children[ch], i + 1)
            
            return ans

        return dfs(cur, 0)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)