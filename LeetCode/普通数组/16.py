def profictExcel(nums:list[int])->list[int]:
    n = len(nums)
    right = [1]*n
    for i in range(1,n):
        right[i] = right[i-1]*nums[i-1]
    
    left = [1]*n
    for i in range(n-2,-1,-1):
        left[i] = left[i+1]*nums[i+1]
    
    return [l*r for l,r in zip(left,right)]

print(profictExcel([1,2,3,4]))