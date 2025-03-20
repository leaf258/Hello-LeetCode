from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0

        while left<right:
            width = right - left
            min_heigh = min(height[left], height[right])
            current_water = width*min_heigh

            max_water = max(max_water, current_water)

            # 比较两个指针所指向的高度，将较短的那个指针向内移动一位（因为移动较长垂线的指针无法增加水量，而移动较短垂线的指针可能找到更高的垂线来增加水量）
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_water

height = [1,8,6,2,5,4,8,3,7]
solution=Solution()
print(solution.maxArea(height))  # 输出49，对应(1, 8)和(7, 4)两条线构成的容器
