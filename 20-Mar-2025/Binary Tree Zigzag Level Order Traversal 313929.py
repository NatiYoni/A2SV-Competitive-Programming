# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = defaultdict(list)

        def bfs(root,depth):

            if not root:
                return 
            
            level[depth].append(root.val)

            bfs(root.left, depth + 1)
            bfs(root.right, depth + 1)
            # print(level)

            
        
        bfs(root, 0)
        return [val if d % 2 == 0 else val[::-1] for d, val in level.items()]

            
