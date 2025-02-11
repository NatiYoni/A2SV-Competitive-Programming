# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p1 = str(nums[i]) + str(nums[j])
                p2 =  str(nums[j]) + str(nums[i])

                if int(p1) < int(p2):
                    nums[i], nums[j] = nums[j], nums[i]

        for index, num in enumerate(nums):
            nums[index] = str(num)
        
        result = "".join(nums)

        return str(int(result))

                
    #     temp = [str(num) for num in nums]
    #     max_length = max(len(num) for num in temp)
        
    #     for i in range(len(temp)):
    #         for j in range(i + 1,len(temp)):
    #             min_length = min(temp[i],temp[j])

    #             if int(temp[j][:min_length]) > int(temp[i][:min_length]):
    #                 temp[i], temp[j] = temp[j], temp[i]
    #             elif int(temp[j][:min_length]) = int(temp[i][:min_length]):
    #                 if int(temp[j][:min_length]) = int(temp[i][:min_length])

    #             # if int(temp[j] + "0" * (max_length - len(temp[j]))) > int(temp[i] + "0" * (max_length - len(temp[i]))):
    #             #     temp[i], temp[j] = temp[j], temp[i]
                    
    #             # elif int(temp[j] + "0" * (max_length - len(temp[j]))) == int(temp[i] + "0" * (max_length - len(temp[i]))):
    #             #     if len(temp[j]) < len(temp[i]):
    #             #         temp[i], temp[j] = temp[j], temp[i]
                        
    #     return "".join(temp)



        