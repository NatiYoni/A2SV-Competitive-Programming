# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _map =  {}
        for i in range(len(names)):
            _map[heights[i]] = names[i]

        heights.sort(reverse = True)

        for index,height in enumerate(heights):
            names[index] = _map[height]
        
        return names

         