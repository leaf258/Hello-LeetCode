
class DP:
# 给定一个楼梯，你每步可以上 1 阶或者 2 阶，每一阶楼梯上都贴有一个非负整数，表示你在该台阶所需要付出的代价。给定一个非负整数数组 cost ，其中 cost[i] 表示在第 i 个台阶需要付出的代价，0 为地面（起始点）。请计算最少需要付出多少代价才能到达顶部？
    def min_cost_climbing_stairs_dp(self, cost:list):
        n = len(cost)
        if n == 1 or n == 2:
            return cost[n]
        dp = [0]*(n)
        dp[1], dp[2] = cost[1], cost[2]
        for i in range(3, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[n-1]

    # 空间优化
    def min_cost_climbing_stairs_dp_comp(self, cost:list):
        n = len(cost)
        if n == 1 or n == 2:
            return cost[n]
        a, b = cost[1], cost[2]
        for i in range(3, n):
            a, b = b, min(a, b)+cost[i]
        return b
    
# 给定一个共有 n 阶的楼梯，你每步可以上 1 阶或者 2 阶，但不能连续两轮跳 1 阶，请问有多少种方案可以爬到楼顶？
# dp[i,1] = dp[i-1,2]              # i 状态上了1阶，则i-1状态只可能上了2阶
# dp[i,2] = dp[i-2,1] + dp[i-2,2]  # i 状态上了2阶，则i-1状态可能上1阶也可能上2阶
# 即下一步选择不能由当前状态（当前所在楼梯阶数）独立决定，还和前一个状态（上一轮所在楼梯阶数）有关。
    def climbing_stairs_constrain_dp(self, n:int):
        if n == 1 or n == 2:
            return 1
        dp = [[0]*3 for _ in range(n+1)] # 通过列表推导式，​每一行是独立的新列表，避免引用问题。
            #错误写法：dp = [[0] * 3] * (n + 1) 所有行是同一个列表的引用！dp[0][0] = 1 修改后所有行的第0列都会变成1！
        dp[1][1], dp[1][2] = 1,0
        dp[2][1], dp[2][2] = 0,1
        for i in range(3,n+1):  # 从状态i=3开始
            dp[i][1] = dp[i-1][2]
            dp[i][2] = dp[i-2][1] + dp[i-2][2]
        return dp[n][1]+dp[n][2]





def main():
    cost = [0,1,10,1]
    dp = DP()
    # print(dp.min_cost_climbing_stairs_dp(cost))
    # print(dp.min_cost_climbing_stairs_dp_comp(cost))
    print(dp.climbing_stairs_constrain_dp(3))

if __name__ == "__main__":
    main()