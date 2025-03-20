# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}  # 字典存储值到索引的映射
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in hash_map:
#                 return [hash_map[complement], i]  # 返回complement的索引和当前索引
#             hash_map[num] = i  # 存储num到其索引的映射
#         return []

# # 测试代码
# test_num = [2, 7, 11, 15]
# test_target = 9
# solution = Solution()  # 创建Solution类的实例
# result = solution.twoSum(nums=test_num, target=test_target)  # 调用实例方法
# print(result)  # 输出结果应该是 [0, 1]


dic = {5:["0","2"], 7:["1"], 6:2}
# value = list(dic.values())
print(dic[5]) # python输出一个字典中键对应的值
# python输出一个字典中当前值对应的键
for key, values in dic.items():
    if values == 2:
        print(key)
        dic[7].append("9")
        print(dic[7])