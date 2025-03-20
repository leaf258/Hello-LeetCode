# Counter是Python标准库collections模块中的一个类，用于计数可哈希对象。它是一个字典子类，其中元素作为键，其计数作为值。这个类特别有用于计数可迭代对象中的元素出现的次数。
from collections import Counter

# # 创建一个Counter对象
# cnt_s = Counter()
# cnt_t = Counter()

# # # 可以直接传递一个可迭代对象给Counter进行计数
# # # 例如，这里传递一个列表
# # items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# # cnt_t = Counter(items)

# cnt_s['a'] += 2
# cnt_s['a'] += 1
# print(cnt_s - cnt_t)

# # 打印结果
# print(cnt_s)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数

        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            while cnt_s >= cnt_t:  # 涵盖
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

solution = Solution() 
s = "ADOBECODEBANC"
t = "ABC"
result = solution.minWindow(s=s, t=t)
print(result)

