# dp[i,j] = min(dp[i-1,j], dp[i, j-1]) + grid[i,j]
from numpy import inf

# 暴力搜索（从顶部n至底部0运算）
def min_path_sum_dfs(grid:list[list], i:int, j:int):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return inf
    up = min_path_sum_dfs(grid, i-1, j)
    left = min_path_sum_dfs(grid, i, j-1)
    return min(left,up)+grid[i][j]

# 暴力搜索+加入记忆，避免重复运算
def min_path_sum_dfs_mem(grid:list[list], row:int, column:int, mem:list[list]):
    if row == 0 and column == 0:
        return grid[0][0]
    if row < 0 or column < 0:
        return inf # 返回inf的作用是，在比较的时候，如果某条路径越界，其值会是无穷大，这样min函数就会自动忽略这条路径，选择另一条有效的路径。而如果直接return的话，返回None，min函数无法处理，导致TypeError。
    if mem[row][column] != -1:
        return mem[row][column]
    up = min_path_sum_dfs_mem(grid, row-1, column, mem)
    left = min_path_sum_dfs_mem(grid, row, column-1, mem)
    mem[row][column] = min(up,left) + grid[row][column]
    return mem[row][column]

# 动态规划（从底部0至顶部n运算）(要先将所有边界条件给出)
def min_sum_path_dp(grid:list[list]):
    n = len(grid) # n行
    m = len(grid[0]) # m列
    # 初始化 dp 表
    dp = [[0]*(m) for _ in range(n)] # n行m列
    dp[0][0] = grid[0][0]
    # 状态转移：首列
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    # 状态转移：首行
    for j in range(1,m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    # 状态转移：其余行和列
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[n-1][m-1]

# 动态优化+空间优化




def main():
    grid = [[1,3,1,5],[2,2,4,2],[5,3,2,1]]  # ,[4,3,5,2]
    # print(min_path_sum_dfs(grid, len(grid)-1, len(grid[0])-1))  # 输入网格grid，grid的行值-1，grid的列值-1
    mem = [[-1]*4,[-1]*4,[-1]*4]
    print(min_path_sum_dfs_mem(grid, len(grid)-1, len(grid[0])-1, mem))
    print(min_sum_path_dp(grid))


if __name__ == "__main__":
    main()