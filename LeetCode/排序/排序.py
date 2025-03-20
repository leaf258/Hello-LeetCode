# 选择排序：开启一个循环，每轮从未排序区间选择最小的元素，将其放到已排序区间的末尾。
# 非稳定排序: 排序过程中给，相等元素在数组中的相对顺序可能发生改变
# 时间复杂度为 O(n^2)，空间复杂度O(1)
def select_sort(nums):
    if not nums:
        return 
    n = len(nums)
    for i in range(n-1): # range(n-1)是左闭右开的,从0，1，2，……，n-2
    # eg:选取区间[0,n-1] 中的最小元素，将其与索引0 处的元素交换。完成后，数组前 1 个元素已排序。
        k = i
        for j in range(i+1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums


# 冒泡排序：连续地比较与交换相邻元素实现排序
# 稳定排序：在“冒泡”中遇到相等元素不交换。
# 时间复杂度仍为 O(n^2)，空间复杂度O(1)
def bubble_sort(nums:list):
    if not nums:
        return 
    n = len(nums)
    for i in range(n-1, 0, -1): # range(n-1, 0, -1) 左闭右开，从n-1,n-2,……,1，每次递减1
        flag = False # 初始化标志位(效率优化)
        # 经过优化，冒泡排序的最差时间复杂度和平均时间复杂度仍为 O(n^2)；但当输入数组完全有序时，可达到最佳时间复杂度O(n)
        for j in range(i): # 对前i-1个元素进行排序，选出最大的那个放在第i-1位
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break  # 如果这一轮没有进行任何交换，说明当前数组已经完成排序，直接跳出for循环不再执行
    return nums


# 插入排序：在未排序区间选择一个基准元素，将该元素与其左侧已排序区间的元素逐一比较大小，并将该元素插入到正确的位置。
# 稳定排序：在插入操作过程中，我们会将元素插入到相等元素的右侧，不会改变它们的顺序。
# 时间复杂度仍为 O(n^2)，空间复杂度O(1)
def insertion_sort(nums:list):
    if not nums:
        return
    n = len(nums)
    for i in range(1,n):
        base = nums[i]
    # while循环实现
        j = i-1
        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = base
    # for循环实现
        # for j in range(i-1,-1,-1):
        #     if nums[j] > base:
        #         nums[j+1] = nums[j]
        #         nums[j] = base
        #         break
    return nums


# 快速排序
# 时间复杂度为O(nlogn) ，空间复杂度为O(n)
# 非稳定排序：在哨兵划分的最后一步，基准数可能会被交换至相等元素的右侧。
class QuickSorted:
    def partition(self, nums:list, left:int, right:int):
        i, j = left, right
        base = nums[left]  # 以 nums[left] 为基准数
        while i < j:
            while i < j and nums[j] >= base: # 直到右边遇到 x1<base, 停止(从右向左找首个小于基准数的元素)
                j -= 1  
            while i < j and nums[i] <= base: # 直到左边遇到 x2>base, 停止(从左向右找首个大于基准数的元素)
                i += 1 
            nums[i], nums[j] = nums[j], nums[i] # 交换x2 x1
        nums[i], nums[left] = nums[left], nums[i] # 交换base x1, 得到目前顺序 ...x1(left)...base(i)...x2(j)...
        return i 
    
    def quicksort(self, nums:list, left:int, right:int):
        # 子数组长度为 1 时终止递归
        if left >= right:
            return
        pivot = self.partition(nums = nums, left = left, right = right) # 得到基准数跟新的位置
        # 先递归左子数组
        self.quicksort(nums, left = left, right = pivot-1)
        # 再递归右子数组
        self.quicksort(nums, left = pivot + 1, right = right)

    def median_three(self, nums, left, mid, right):
        le, mi ,ri = nums[left], nums[mid], nums[right]
        if le < mi <ri:
            return mid
        if mi < le < ri:
            return left
        return right
    
    def partition_median(self, nums, left, mid, right):
        i, j = left, right
        median = self.median_three(nums, left, mid, right) # 找到中位数索引
        nums[left], nums[median] = nums[median], nums[left] # 将中位数放到最左边
        base = nums[left] # 基准数
        while i < j:
            while i < j and nums[i] <= base: # 左边找到 xi>base
                i += 1
            while i < j and nums[j] >= base: # 右边找到 xj<base
                right -= 1
            nums[i], nums[j] = nums[j], nums[i] # base xj xi
        nums[left], nums[i] = nums[i], nums[left] # xj base xi
        return i 
        


# / 是普通的除法，返回浮点数结果；
# // 是取整除，返回商向下取整的结果；
# % 是取模，返回余数，结果的符号与除数相同。
        



def main():
    nums = [2,3,1,4,3,5] # [1,3,1,2]
    # res_select = select_sort(nums)
    # print(res_select)
    # res_bubble = bubble_sort(nums)
    # print(res_bubble)
    # res_insertion = insertion_sort(nums)
    # print(res_insertion)
    quicksorted = QuickSorted()
    quicksorted.quicksort(nums=nums, left=0, right=len(nums)-1)
    print(nums)

if __name__ == "__main__":
    main()