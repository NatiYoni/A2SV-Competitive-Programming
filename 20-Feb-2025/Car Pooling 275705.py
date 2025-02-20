# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0] * 1002

        for ca, start, end in trips:
            car[start] += ca
            car[end] -= ca
        
        for i in range(1,1001):
            car[i] += car[i-1]


        for i in range(1001):
            if car[i] > capacity:
                return False

        return True
            

        
