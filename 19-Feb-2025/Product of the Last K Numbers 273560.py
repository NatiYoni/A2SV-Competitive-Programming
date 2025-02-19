# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.multi = 1
        self.pointer = 0
        self.flag = False
        
    def add(self, num: int) -> None:
        self.multi = self.multi * num

        if self.multi == 0:
            self.flag = True
            self.pointer = len(self.nums)
            self.nums.append(self.multi)
            self.multi = 1

        else:
            self.nums.append(self.multi)
            
        

    def getProduct(self, k: int) -> int:
        print(len(self.nums) - k)

        if len(self.nums) - k <= self.pointer and self.flag:
            return 0 
        elif len(self.nums) - k - 1 == self.pointer and self.flag:
            return self.nums[-1]
        elif len(self.nums) == k:
            return self.nums[-1]
        else:
            return self.nums[-1] // self.nums[len(self.nums)-k-1]
        
        
   
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)