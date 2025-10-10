# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.is_end = False
        self.child = [None] * 26
        
        self.root = None

    def insert(self, word: str) -> None:
        if not self.root:
            self.root = Trie()

        cur = self.root
        n = len(word)

        for i,l in enumerate(word):
            idx = ord(l) - 97
            if not cur.child[idx]:
                cur.child[idx] = Trie()
            
            cur = cur.child[idx]
            if i ==n-1:
                cur.is_end = True
            
   
    def search(self, word: str) -> bool:
        if not self.root:
            self.root = Trie()

        cur = self.root
        n = len(word)
        for  i,l in enumerate(word):
            idx = ord(l) - 97
            if not cur.child[idx]:
                return False
            
            cur = cur.child[idx]
            if i == len(word) -1:
                return True if cur.is_end else False
                
           

        
    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            self.root = Trie()

        cur = self.root
        
        for l in prefix:
            idx = ord(l) - 97
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)