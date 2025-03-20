from typing import List
from collections import defaultdict
#在Python的collections模块中，defaultdict扩展了内置的dict类型。
# #defaultdict的一个独特之处在于，当尝试访问字典中不存在的键时，它不会抛出KeyError异常，而是会返回一个默认值。
# 当你使用collections.defaultdict(list)时，你创建了一个默认值为空列表（[]）的字典。这意味着，每当你尝试访问一个尚未在字典中定义的键时，defaultdict会自动为该键创建一个空列表作为值，而不是返回KeyError或None。

# 这在处理具有嵌套数据结构的数据时特别有用，比如当你想要将一系列元素分组到不同的类别中，而这些类别在开始时可能并不存在于字典中。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # 使用默认字典简化代码
        for s in strs:
            key = ''.join(sorted(s))  # 排序后字符串作为键
            groups[key].append(s)     # 直接添加当前字符串
        return list(groups.values())
    

test_strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()

result = solution.groupAnagrams(strs=test_strs)
print(result)