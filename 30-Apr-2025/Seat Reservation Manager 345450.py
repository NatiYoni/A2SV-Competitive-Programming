# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.arr = [i for i in range(1,n+1)] 
        
        heapify(self.arr)

    def reserve(self) -> int:
        if self.arr:
            val = heappop(self.arr)
        
            return val


    def unreserve(self, seatNumber: int) -> None:
        
        heappush(self.arr,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)