from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        water_sum = 0

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            # 当左边水位小于右边时，左边一定能存下水
            if height[left] < height[right]:
                water_sum += left_max - height[left]
                left += 1
            else:
                water_sum += right_max-height[right]
                right -= 1
        return water_sum
    

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
test_height = [0,1,0,0,0,0,0,0,0,0,0,1]
result = solution.trap(test_height)
print(result)