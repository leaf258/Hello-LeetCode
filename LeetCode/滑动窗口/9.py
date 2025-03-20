from typing import Counter, List

# Counter用于计数可哈希对象。它主要用于统计一个可迭代对象中各个元素出现的次数。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口
            left = right - len(p) + 1
            if left < 0:  # 窗口长度不足 len(p)
                continue
            if cnt_s == cnt_p:  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
            cnt_s[s[left]] -= 1  # 左端点字母离开窗口
        return ans

solution = Solution() 
s_test = "cbaebabacd"
p_test = "abc"
result = solution.findAnagrams(s = s_test, p = p_test)
print(result)




# count = [0,1,0]

# differ = 0

# for c in count:
#     if c != 0:
#         differ += 1

# print(differ)

# count.append(1)

# print(count)

# s = "cbaebabacd"
# p = "abc"
# print(Counter(s))