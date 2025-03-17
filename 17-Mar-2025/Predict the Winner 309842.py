# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        
        def play(l, r):
            
            if l == r:
                return nums[l]
                
            return max(nums[l] - play(l + 1, r), nums[r] - play(l, r - 1))
        
        return play(0, len(nums) - 1) >= 0