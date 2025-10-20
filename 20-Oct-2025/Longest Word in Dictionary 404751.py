# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
    

class trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, s):
        cur = self.root

        for i,l in enumerate(s):
            ch = ord(l)-97

            if not cur.children[ch]:
                cur.children[ch] = TrieNode()
                    
            cur = cur.children[ch]
        
        cur.end = True
        
    def dfs(self,node, path):
        
        if not node or not node.end: return path[:-1]
        
        ans = path
        for i in range(26):
            child = node.children[i]
            if child and child.end:
                temp = self.dfs(child, path + chr(i + 97))
                if len(temp) > len(ans) or (len(temp) == len(ans) and temp < ans):
                    ans = temp
        
        return ans



class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = trie()
        
        for word in words:
            t.insert(word)
        
        ans = []
        for i in range(26):
            child = t.root.children[i]
            if child and child.end:
                temp = t.dfs(child, chr(i + 97)) 
                if len(temp) > len(ans) or (len(temp) == len(ans) and temp < ans):
                    ans = temp[:]
        
        return "".join(ans)