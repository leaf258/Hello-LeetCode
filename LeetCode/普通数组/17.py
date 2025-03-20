def firstMissiingPostive(nums:list[int]) -> int:
    n = len(nums)
    hash_size = n+1
    for i in range(n):
        if nums[i]<=0 or nums[i]>n:
            nums[i] = 0
    for i in range(n):
        if nums[i] % hash_size != 0:
            pos = nums[i] % hash_size - 1
            nums[pos] = nums[pos] % hash_size + hash_size
    for i in range(n):
        if nums[i] < hash_size:
            return i + 1
    return hash_size

print(firstMissiingPostive(nums = [3,4,-1,1]))