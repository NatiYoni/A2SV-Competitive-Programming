# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dq = deque()
        if root:
            dq.append((root, root.val))

        ans = 0
        visited = set()

        while dq:
            node, val = dq.pop()

            if node.left :
                curleft = val + node.left.val
                
                dq.append((node.left, curleft))
                if node.left not in visited:
                    dq.append((node.left, node.left.val))
                    visited.add(node.left)
                
            
            if node.right:
                curright = val  + node.right.val

                
                dq.append((node.right, curright))
                if node.right not in visited:
                    dq.append((node.right, node.right.val))
                    visited.add(node.right)

            if val == targetSum:
                ans += 1
        
            
        
        return ans
                
