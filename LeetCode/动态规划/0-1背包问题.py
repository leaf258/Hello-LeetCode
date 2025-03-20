# 给定 n 个物品，第 i 个物品的重量为 wgt[i-1]、价值为 val[i-1] ，和一个容量为 cap 的背包。每个物品只能选择一次，问在限定背包容量下能放入物品的最大价值。
# 当前物品编号 i 和背包容量 c
# 状态 [i,c] 对应的子问题为：前 i 个物品在容量为 c 的背包中的最大价值，记为 dp[i,c], 待求解dp[n,cap]
# dp[i,c] = max(dp[i-1,c], dp[i-1,c-wgt[i-1]] + val[i-1])

class Solution:
# 暴力搜索（纯递归）# 从顶到底
    def kanpsack_dfs(self, wgt:list, val:list, i:int, c:int):
        if i == 0 or c == 0:
            return 0
        if wgt[i-1] > c:
            return self.kanpsack_dfs(wgt=wgt, val=val, i=i-1, c=c)
        yes = self.kanpsack_dfs(wgt=wgt, val=val, i=i-1, c=c-wgt[i-1]) + val[i-1]
        no = self.kanpsack_dfs(wgt=wgt, val=val, i=i-1, c=c)
        return max(yes,no)

    # 记忆搜索
    def kanpsack_mem_dfs(self, wgt:list, val:list, i:int, c:int, mem:list):
        if i == 0 or c == 0:
            return 0
        if wgt[i-1] > c:
            return self.kanpsack_mem_dfs(wgt=wgt, val=val, i=i-1, c=c)
        if mem[i-1] != -1:
            return mem[i-1]
        yes = self.kanpsack_mem_dfs(wgt=wgt, val=val, i=i-1, c=c-wgt[i-1], mem = mem) + val[i-1]
        no = self.kanpsack_mem_dfs(wgt=wgt, val=val, i=i-1, c=c, mem = mem)
        mem[i-1] = max(yes, no)
        return mem[i-1]
    
    def kanpsack_memij_dfs(self, wgt:list, val:list, i:int, c:int, mem:list[list]):
        if i == 0 or c == 0:
            return 0
        if wgt[i-1] > c:
            return self.kanpsack_memij_dfs(wgt=wgt, val=val, i=i-1, c=c, mem=mem)
        if mem[i][c] != 0:
            return mem[i][c]
        yes = self.kanpsack_memij_dfs(wgt=wgt, val=val, i=i-1, c=c-wgt[i-1], mem = mem) + val[i-1]
        no = self.kanpsack_memij_dfs(wgt=wgt, val=val, i=i-1, c=c, mem = mem)
        mem[i][c] = max(yes, no)
        return mem[i][c]

# 动态规划(从底到顶)
    def kanpsack_dp(self, wgt:list, val:list, cap:int):
        n = len(wgt)
        dp = [[0]*(cap+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for c in range(1, cap+1):
                if wgt[i-1] > c:
                    dp[i][c] = dp[i-1][c]
                else:
                    dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt[i-1]]+val[i-1])
        return dp[n][cap]

    # 空间优化
    def kanpsack_dp_comp(self, wgt:list, val:list, cap:int):
        n = len(wgt)
        dp = [0]*(cap+1)
        for i in range(n+1):
            for c in range(cap, 0, -1):
                if wgt[i-1] > c:
                    dp[c] = dp[c]
                else:
                    dp[c] = max(dp[c], dp[c-wgt[i-1]]+val[i-1])
        return dp[cap]


def main():
    solution = Solution()
    weight = [10,20,30,40,50]
    value = [50,120,150,210,240]
    n= 5
    cap = 50
    # res = solution.kanpsack_dfs(wgt = weight, val = value, i = n, c = cap)
    # print(res)
    mem = [-1]*n
    mem_i_j = [[0]*(cap+1) for _ in range(n+1)]
    # mem_res = solution.kanpsack_mem_dfs(wgt = weight, val = value, i = n, c = cap,mem=mem)
    # memij_res = solution.kanpsack_memij_dfs(wgt = weight, val = value, i = n, c = cap,mem=mem_i_j)
    # print(memij_res)
    # print(solution.kanpsack_dp(wgt=weight, val= value, cap=cap))
    print(solution.kanpsack_dp_comp(wgt=weight, val=value, cap=cap))


if __name__ == "__main__":
    main()