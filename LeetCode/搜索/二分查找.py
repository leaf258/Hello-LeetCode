def dfs_search(nums:list, target:int, i:int, j:int) -> int:
    if not nums:
        return -1
    mid = (i+j)//2
    if nums[mid] > target:
        return dfs_search(nums, target, i, mid-1) # 在递归调用dfs_search()后，没有使用return将结果传递回上层调用，则无法返回结果。
    elif nums[mid] < target:
        return dfs_search(nums, target, mid+1, j)
    else:
        return mid


def binary_search(nums:list, target:int) -> int:
    i, j = 0, len(nums)-1
    while i < j:
        mid = (i+j)//2
        if nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
        else:
            return mid
    return -1

    
if __name__=="__main__":
    nums = [1,2,3,4,5,6]
    res = dfs_search(nums=nums, target=5, i=0, j=len(nums)-1)
    print(res)
    # result = binary_search(nums, 5)
    # print(result)