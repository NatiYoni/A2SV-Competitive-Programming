# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for path in logs:

            if path == "../":
                if stack:
                    stack.pop()
                else:
                    continue

            elif path == "./":
                continue
            
            else:
                stack.append(path)
        
        return len(stack)
            
            
            