# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        dq = deque()
        dq.append(root)

        level = 0
        while dq:
                level += 1
                for i in range(len(dq)):
                    node = dq.popleft()
                    
                    for chld in node.children:
                        dq.append(chld)
            
        return level