# 指令“Do not return anything, modify nums in-place instead”，这意味着你不需要通过函数返回值来改变数据，而是应该直接在函数内部修改传入的参数

def rotate(nums: list[int], k: int) -> None:
    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k %= n
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    return nums

test_nums=[1,2,3,4,5,6,7]
rotate(nums=test_nums, k=3)
print(test_nums)

