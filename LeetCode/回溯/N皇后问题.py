def backtrack(
        n:int,
        row:int, 
        state:list[list],  # 保存当前棋盘结果
        res:list[list[list]],  # 保存所有棋盘结果
        cols:list[bool], 
        digs1:list[bool], 
        digs2:list[bool]):
    if row == n:
        res.append([list(row) for row in state])
        return
    for col in range(n):
        dig1 = row - col + n -1 # 保证索引从0开始
        dig2 = row + col
        if not cols[col] and not digs1[dig1] and not digs2[dig2]:
            state[row][col] = "Q"
            cols[col] = digs1[dig1] = digs2[dig2] = True
            backtrack(n, row+1, state, res, cols, digs1, digs2)
            state[row][col] = "#"
            cols[col] = digs1[dig1] = digs2[dig2] = False
            

def n_queens():
    n = 4
    row = 0
    state = [['#' for _ in range(n)] for _ in range(n)]
    res = []
    cols = [False]*n
    digs1 = [False]*(2*n-1)
    digs2 = [False]*(2*n-1)
    backtrack(n, row, state, res, cols, digs1, digs2)
    return res


if __name__ == "__main__":
    a = n_queens()
    print(a)