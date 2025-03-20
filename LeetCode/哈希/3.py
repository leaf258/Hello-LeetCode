from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums) # set 是一种内置的数据结构，它表示一个无序不重复的元素集合。当你执行 num_set = set(nums) 时，你正在使用 set 构造函数或称为 set 类型的一个转换功能，将列表（或其他可迭代对象）nums 中的元素转换成一个集合。
        # num_set = set(nums) 创建了一个包含 nums 列表中所有唯一元素的集合。这个集合随后被用于快速检查某个数字是否存在于原始列表中，这是解决最长连续序列问题的一个关键步骤。
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
nums = [100,4,200,1,3,2]
solution=Solution()
result = solution.longestConsecutive(nums=nums)
print(result)