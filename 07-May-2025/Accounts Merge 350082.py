# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = [i for i in range(len(accounts))]
        meta = [1 for i in range(len(accounts))]
        memo = defaultdict(int)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x
        
        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            if x_ != y_:
                if meta[x_] < meta[y_]:
                    x_, y_ = y_, x_
                    meta
                parent[y_] = x_
                meta[x_] += meta[y_]


        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in memo and memo[accounts[i][j]] != i:

                    union(i,memo[accounts[i][j]])
                    # print(i,parent)
                   
                
                memo[accounts[i][j]] = i


        
        temp_ans = defaultdict(set)

        # print(parent)
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                temp_ans[find(i)].add(accounts[i][j])
        
        ans = []
        for key in temp_ans.keys():
            temp = []
            temp.append(accounts[key][0])
            temp.extend(sorted(list(temp_ans[key])))

            ans.append(temp)
        # print(parent)
        # print(temp_ans)
        return ans
                