# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:

        heappush(self.small, -1 *  num)

        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            heappush(self.large,-1 * heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -1* heappop(self.small))
        
        if len(self.small) + 1 < len(self.large) :
            heappush(self.small, -(heappop(self.large)))


    def findMedian(self) -> float:

        if len(self.large) < len(self.small):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        else:
            return (-1 * self.small[0] + self.large[0]) / 2

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()