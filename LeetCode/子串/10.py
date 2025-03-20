from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0]*(len(nums)+1)
        for i, num in enumerate(nums):
            s[i+1] = s[i] + num

        count = 0

        for j in range(len(s)):  # j为右指针
            for i in range(j):   # i为左指针
                if s[j] == s[i] + k:
                    count += 1

        return count
    
solution = Solution() 
nums_test = [1,1,1]
result = solution.subarraySum(nums=nums_test, k=2)
print(result)