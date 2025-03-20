def merge(intervals:list[list[int]]) -> list[list[int]]:
    intervals.sort(key = lambda p : p[0])
    result = []

#     这个条件语句首先检查 result 是否为真值（在Python中，非空列表、元组等被认为是真值）。
# 如果 result 为真（即，它不是一个空列表或空的可迭代对象），那么它会继续检查 p[0] <= result[-1][1]。
# 这个比较检查当前元组 p 的起始点是否小于或等于 result 列表中最后一个区间的结束点。
    for p in intervals:
        if result and p[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], p[1])
        else:
            result.append(p)
    return result

intervals =[[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals=intervals))