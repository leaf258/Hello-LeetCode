def length_of_longest_substring(s: str) -> int:
    # 字典用于存储字符及其索引
    dic = {}
    # 初始化窗口的左右边界
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # 如果字符已经在窗口中，则更新左边界
        if s[right] in dic and dic[s[right]] >= left:
            left = dic[s[right]] + 1
        
        # 更新字符的索引
        dic[s[right]] = right
        
        # 计算当前窗口的长度并更新最大长度
        max_length = max(max_length, right - left + 1)
    
    return max_length

# 示例测试
s = "abcabcbb"
print(length_of_longest_substring(s))  # 输出: 3