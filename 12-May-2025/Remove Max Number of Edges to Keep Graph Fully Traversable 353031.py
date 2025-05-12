# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = [i for i in range(n)]
        alice_size = [1 for i in range(n)]
        bob = [i for i in range(n)]
        bob_size = [1 for i in range(n)]
        ans = [0]
        edges.sort(key = lambda x : x[0],reverse = True)

        def find(x,parent,size):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y,parent,size):
            x_ = find(x,parent,size)
            y_ = find(y,parent,size)
            
            if x_ != y_:
                if size[x_] < size[y_]:
                    x_, y_ = y_, x_
            
                parent[y_] = x_
                
                size[x_]+= size[y_]
            else:
                return False
            
            return True
            
        ans = 0
        for t,x,y in edges:
            if t == 1:
                val = union(x-1,y-1,alice,alice_size)
                if not val:
                    ans += 1
            elif t == 2:
                val = union(x-1,y-1,bob,bob_size)

                if not val:
                    ans += 1
            else:
                val1 = union(x-1,y-1,alice,alice_size)
                val2 = union(x-1,y-1,bob,bob_size)

                if not val1 or not val2:
                    ans += 1
        
        seen_alice = set()
        seen_bob = set()
        for i in range(n):
            val1 = find(i,alice,alice_size)
            seen_alice.add(val1)
            val2 = find(i,bob,bob_size)
            seen_bob.add(val2)
            

            if len(seen_alice) > 1 or len(seen_bob) > 1:
                return -1

        return ans