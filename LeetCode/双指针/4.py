from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # 在Python中，多变量赋值语句（如 a, b = b, a）是一种简洁的方式来交换两个变量的值。如果你希望将这个操作分开来写，你可以使用临时变量来辅助完成交换。
                left += 1
            right += 1


test_nums = [0,1,0,3,12]
solution=Solution()
result = solution.moveZeroes(nums=test_nums)
print(result)