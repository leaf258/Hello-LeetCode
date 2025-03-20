# 给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。给定数组无重复元素，每个元素可以被选取多次。请以列表形式返回这些组合，列表中不应包含重复组合。
# 给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。给定数组可能包含重复元素，每个元素只可被选择一次。请以列表形式返回这些组合，列表中不应包含重复组合。

def backtrack(nums:list[int], target:int, total:int, res:list[list],state:list, start:int):
    if total == target:
        res.append(list(state))
        return
    # for i, choice in enumerate(nums):
    #     if total + choice > target:
    #         continue #  触发 continue 时，​不会执行后续任何代码（包括递归和回溯操作）​，而是直接跳过当前候选数，进入循环的下一个迭代。
    #         # break  # 触发break时，​不会执行后续任何代码,直接终止整个循环，不再处理后续候选数
    duplicated = set() # 输入数组可能有重复元素，生成重复子集，剪枝
    for i in range(start,len(nums)): # 剪枝，从 start 开始遍历，避免生成重复子集
        if total + nums[i] > target:
            break  # 因为数组已经经过排序，顾若当前元素大于target，之后的元素也会大于，所以此处直接break终止循环即可
        if nums[i] in duplicated: # 每个数组元素只能被选择一次
            continue # 如果这个元素已经被选过一次，就跳过此元素，继续下一个循环
        duplicated.add(nums[i])

        total += nums[i]
        state.append(nums[i])
        backtrack(nums, target, total, res, state, i) # 递归，继续探索子问题（每次循环从0开始）（个人理解是，在大的循环下不断建立小循环（子树））
        # 当上面的backtrack递归发现total == target时，会return回现在的backtrack，并执行下面的回溯操作
        # 下面两行为回溯操作，恢复父层级状态（eg：当前state=[2,2,3]=target,弹出state并将total恢复为4，继续实验i=2时的total）
        state.pop()
        total -= nums[i]

def main():
    nums = [4,4,5]
    nums.sort() # 排序后，可在backtrack中break以减少操作
    #上面两行可写为 nums = sorted([3,2,6,7])# sorted()函数返回新列表，而sort()方法修改原列表
    # nums.sort()是一个方法调用，它会直接修改原列表，将其排序，返回值为None。而nums.sort本身是一个方法对象，没有被调用。如果用户写成nums.sort，这其实只是引用了这个方法，而不会执行排序操作。
    target = 9
    total = 0
    res = []
    state = []
    start = 0
    backtrack(nums, target, total, res, state, start)
    print(res)
    
if __name__ == "__main__":
    main()