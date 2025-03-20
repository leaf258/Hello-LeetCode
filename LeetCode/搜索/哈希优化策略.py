def two_sum_hash_table(nums:list, target:int):
    dic = {}
    res = []
    for i in range(len(nums)):
        if target - nums[i] in dic:
            # res.append([dic[target-nums[i]], i])
            return [dic[target-nums[i]], i]
        dic[nums[i]] = i
    return []

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    target = 7
    res = two_sum_hash_table(nums=nums, target=target)
    print(res)