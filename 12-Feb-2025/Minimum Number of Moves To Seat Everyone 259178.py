# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        r = 0
        moves = 0
        while r < len(seats):
            moves += abs(seats[r] - students[r])
            r += 1
        
        return moves