from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # 原列表从大到小排序
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue       # 跳过重复的元素
            if nums[i] > 0:
                break          # 提前终止，因为后面的数更大，不可能和为0

            left, right = i+1, n-1

            while left < right:
                total = nums[left] + nums[i] + nums[right]
                if total > 0:
                    right -=1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[left], nums[i], nums[right]])

                    # 跳过重复的元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -=1

        return result
    
solution = Solution()
nums = [-1,0,1,2,-1,-4,-1]
result = solution.threeSum(nums=nums)
print(result)