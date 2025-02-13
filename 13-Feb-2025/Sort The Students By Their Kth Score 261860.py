# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        map_ = {}
        for i in range(len(score)):
            map_[i] = score[i][k]
        
        sorted_map = dict(sorted(map_.items() ,key = lambda item: item[1], reverse=True))
        output = []

        for key in sorted_map.keys():
            output.append(score[key])
        
        return output
