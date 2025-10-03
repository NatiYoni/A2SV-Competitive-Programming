# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        version1 = [int(val) for val in version1]
        version2 = [int(val) for val in version2]

        i  = 0
        while i < len(version1) and i < len(version2):
            if version1[i] > version2[i]:
                return 1
            
            elif version1[i] < version2[i]:
                return -1
            
            i += 1
        
        while  i < len(version1):
            if version1[i] != 0:
                return 1
            
            i+= 1
        
        while  i < len(version2):
            if version2[i] != 0:
                return -1

            i += 1
        return 0

