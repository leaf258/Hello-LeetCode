from numpy import inf


def maxSubArry(nums: list[int]) -> int:
    result = -inf
    current_sum = min_sum = 0

    for num in nums:
        current_sum += num
        result = max(result, current_sum-min_sum)
        min_sum = min(current_sum, min_sum)

    return result

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArry(nums=nums))