# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for l in word:
            ch = ord(l) - 97

            if not cur.children[ch]:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]
        
        cur.end = True

    def search(self, word):
        cur = self.root

        res = []
        for l in word:
            ch = ord(l) - 97
            
            if not cur.children[ch]:
                return word

            res.append(l)
            cur = cur.children[ch]
            if cur.end:
                return "".join(res)
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        
        ans = []
        sentence = sentence.split(" ")
        # print(sentence)
        for word in sentence:
            ans.append(trie.search(word))

        print(ans)
        return " ".join(ans)
        pass