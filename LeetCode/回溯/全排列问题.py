# 输入一个整数数组，其中不包含重复元素，返回所有可能的排列。
# 输入一个整数数组，数组中可能包含重复元素，返回所有不重复的排列。

def backtrack(state:list, choices:list, selected:list[bool], res:list[list]):
    if len(state) == len(choices):
        res.append(list(state))
        #如果需要保存 state 当前的状态，且后续 state 可能会被修改，应该使用 res.append(list(state))。
        # 如果后续不会修改 state，或者希望 res 中的元素和 state 保持同步变化，可以使用 res.append(state)。
        # res.append(list[state])这是错误的语法。在 Python 中，list 是一个内置的类型名，list[state] 试图将 state 作为索引去访问 list 这个类型，这是不合法的操作。list 作为一个类型，不能像列表一样使用索引访问。
        return
    duplicate = set() # 集合 set 是一种无序且元素唯一的数据结构。我们创建一个空集合的方法是使用set()
    for i, choice in enumerate(choices):
        if not selected[i] and choice not in duplicate: # 重复选择剪枝&&相等元素剪枝
            duplicate.add(choice)
            selected[i] = True
            state.append(choice)
            backtrack(state, choices, selected, res) # 递归
            # 回溯
            selected[i] = False
            state.pop()
            
def permutations(nums:list) -> list[list]:
    res = []
    backtrack(state=[], choices=nums, selected=[False]*len(nums), res=res)
    return res

if __name__ == "__main__":
    print(permutations(nums=[1,1,2]))
