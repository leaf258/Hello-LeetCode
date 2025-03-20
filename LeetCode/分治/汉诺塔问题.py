# 在代码中，我们声明一个递归函数 dfs(i, src, buf, tar) ，它的作用是将柱 src 顶部的 i 个圆盘借助缓冲柱 buf 移动至目标柱 tar
def move(src:list[int], tar:list[int]):
    pan = src.pop() # 从 src 顶部拿出一个圆盘
    tar.append(pan) # 将圆盘放入 tar 顶部

def dfs(i:int, src:list[int], buf:list[int], tar:list[int]):
    if i == 1:
        move(src, tar) # 若 src 只剩下一个圆盘，则直接将其移到 tar
        return
    dfs(i-1, src, tar, buf)  # 子问题 f(i-1) ：将 src 顶部 i-1 个圆盘借助 tar 移到 buf
    move(src, tar) # 子问题 f(1) ：将 src 剩余一个圆盘移到 tar
    dfs(i-1, buf, src, tar) # 子问题 f(i-1) ：将 buf 顶部 i-1 个圆盘借助 src 移到 tar

def solve_hanota(A:list[int], B:list[int], C:list[int]):
    n = len(A)
    dfs(n, A, B, C) # 将 A 顶部 n 个圆盘借助 B 移到 C

if __name__ == "__main__":
    A = [1,2,3]
    B = []
    C = []
    solve_hanota(A, B, C)
    print(f"{A}{B}{C}")
