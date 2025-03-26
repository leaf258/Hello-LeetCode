from collections import deque
import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# *args和**kwargs通常用于函数定义中，允许函数接受任意数量的位置参数和关键字参数。*args会将传入的位置参数打包成一个元组，而**kwargs会将关键字参数打包成一个字典。这样在函数调用时，可以灵活地传递参数，而不需要预先定义所有可能的参数。

## 哈希
#选出列表中出现频率最高的两个数
def Toptwo(nums:list) -> list:
    if not nums:
        return
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            dic[nums[i]] += 1
        else:
            dic[nums[i]] = 1
    select_num = sorted(dic.items(), key = lambda x : x[1], reverse=True)[:2]
    return [key for key, val in select_num]


## 二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 层序遍历
def level_order(root:TreeNode):
    res = []
    quene = deque()
    quene.append(root)
    while quene:
        node = quene.popleft()
        res.append(node.val)
        if node.left:
            quene.append(node.left)
        if node.right:
            quene.append(node.right)
    return res
# 前序遍历
def pre_order(root:TreeNode, res:list): # 根 左 右
    if not root:
        return
    res.append(root.val)
    pre_order(root.left, res)
    pre_order(root.right, res)
    return res
# 中序遍历
def in_order(root:TreeNode, res:list): # 左 根 右
    if not root:
        return
    in_order(root.left, res)
    res.append(root.val)
    in_order(root.right, res)
# 后序遍历
def post_order(root:TreeNode, res:list): # 左 右 根 
    if not root:
        return
    post_order(root.left, res)
    post_order(root.right, res)
    res.append(root.val)


## 排序
# 冒泡排序
def bubble_sort(nums:list):
    n = len(nums)
    for i in range(n-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
# 快速排序
def partition(nums:list, left:int, right:int):
    base = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= base: # 找到 base > x2
            j -= 1        # 先减
        while i < j and nums[i] <= base: # 找到 base < x1
            i += 1        # 再加
        nums[i], nums[j] = nums[j], nums[i] # 目前 base x2 x1
    nums[left], nums[i] = nums[i], nums[left]
    return i
def quick_sort(nums, left, right):
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot-1)
    quick_sort(nums, pivot+1, right)


## 回溯
def backtrack(nums:list, target:int, total:int, res:list, state:list) -> list:
    if total == target:
        res.append(list(state))
        return
    duplicated = set()
    for i in range(len(nums)):
        if total + nums[i] > target:
            break
        if nums[i] in duplicated:
            continue
        duplicated.add(nums[i])
        state.append(nums[i])
        total += nums[i]
        backtrack(nums, target, total, res, state)
        state.pop()
        total -= nums[i]

# 分支合并测试










if __name__ == "__main__":
    # nums = [1,1,1,2,3,3]
    # print(Toptwo(nums))
    # nums = [1,3,2,4,1]
    # quick_sort(nums, 0, 4)
    # print(nums)
    nums = [4,4,5]
    nums.sort() # 排序后，可在backtrack中break以减少操作
    target = 9
    total = 0
    res = []
    state = []
    start = 0
    backtrack(nums, target, total, res, state)
    print(res)