# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:

        paths = path.split("/")
        print(paths)

        stack = []

    
        for letter in paths:

            # if letter == "":
            #     # if stack and stack[-1] == "/":
            #     #     stack.pop()
            #     # else:
            #     #     stack.append("/")
            #     pass


            if stack and letter == "..":
                stack.pop()

            # elif letter == ".":
            #     pass

            elif letter != "" and letter != "." and letter != "..":
                stack.append(letter)

            # if stack:
                
                # if stack[-1] == "..":
                #     stack.pop()
                #     stack.pop()
                
                # elif stack[-1] == ".":
                #     stack.pop()

        # print(stack)

        # if stack and stack[-1] == "/":
        #     stack.pop()
        
        

        return "/" + "/".join(stack)
            
            
