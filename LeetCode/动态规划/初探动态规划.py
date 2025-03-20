# 给定一个共有 n 阶的楼梯，你每步可以上 1 阶或者 2 阶，请问有多少种方案可以爬到楼顶？

# 回溯方法
def backtrack(total:int, target:int, res:list, state:list, choices:list):
    if not choices:
        return
    if total == target:
        res.append(list(state))
    for i, choice in enumerate(choices):
        if total < target:
            total += choice
            state.append(choice)
            backtrack(total=total, target=target, res=res, state=state, choices=choices)
            state.pop()
            total -= choice

# 拆解为子问题: 设爬到第 i 阶有 dp[i] 种方法，则 dp[i] = dp[i-1]+dp[i-2]
# 深度优先搜索（DFS）
def dfs(i:int):
    if i == 1 or i == 2:
        return i
    count = dfs(i-1) + dfs(i-2)
    return count
# 记忆化搜索（递归）# 经过记忆化处理后，所有重叠子问题都只需计算一次，时间复杂度优化至 O(n)
def dfs_mem(i:int, mem:list):
    if i == 1 or i == 2:
        return i
    if mem[i] != -1: # 说明 mem[i]=dp[i] 已经被计算过了，有值
        return # 此时不进行下面的递归，回到上一步
    count = dfs_mem(i-1, mem) + dfs_mem(i-2, mem)
    mem[i] = count
    return count
# 动态规划（从底至顶）
def climbing_stairs_dp(n:int):
    if n==1 or n==2:
        return n
    dp = [0]*(n+1)
    dp[1], dp[2] = 1,2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
# 空间优化，只留下2个变量向前滚动
def climbing_stairs_dp_comp(n:int):
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b





def main():
# 回溯
    total = 0
    target = 3 # 3 阶楼梯
    res = []
    state = []
    choices = [1,2] # 每次可选择1次或2次
    backtrack(total=total, target=target, res=res, state=state, choices=choices)
    print(res)
    print(len(res))
    # print(res.count()) # 在Python中，list.count(x) 方法需要一个明确的参数来指定要统计的目标元素x。因为 count(x) 方法的设计目的是统计特定元素x在列表中出现的次数。
# 递归（从顶至底）
    print(dfs(3))
# 记忆化搜索（递归）# 经过记忆化处理后，所有重叠子问题都只需计算一次，时间复杂度优化至 O(n)
    dp = [-1]*4 # 最终要求的是dp[3],多出的dp[0]不参与计算
    print(dfs_mem(3, mem=dp))
# 动态规划（从底至顶）
    print(climbing_stairs_dp(3))
    print(climbing_stairs_dp_comp(3))


if __name__ == "__main__":
    main()