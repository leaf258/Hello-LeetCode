# 当数组不包含 target 时，最终 i 和 j 会分别指向首个大于、小于 target 的元素。

# 二分查找插入点（无重复元素）
def binary_search_insertion(nums:list, target:int) -> int:
    if not nums:
        return -1
    i, j = 0, len(nums)-1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] > target:
            j = mid-1
        elif nums[mid] < target:
            i = mid+1
        else:
            return mid # 当数组包含 target 时，插入点的索引就是该 target 的索引。
    return i # 当数组不包含 target 时，插入索引为 i

# 二分查找插入点（有重复元素）
def binary_search_insertion_(nums:list, target:int) -> int:
    if not nums:
        return -1
    i, j = 0, len(nums)-1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1 # 当 nums[mid] = target 时，继续向左遍历
    return i 



    
if __name__=="__main__":
    nums = [1,2,3,4,5,5,5,5,6,7]
    res = binary_search_insertion_(nums=nums, target=5)
    print(res)