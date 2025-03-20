from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque() 
        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i>=k-1:
                result.append(nums[q[0]])
        return result
    
test_nums = [1,3,-1,-3,5,3,6,7]
test_k = 3
solution = Solution() 
result = solution.maxSlidingWindow(nums=test_nums,k=test_k)
print(result)


# q = deque() 
# q.append([1,3])
# q.append([2,4])
# q.append([3,5])
# q.append([4,6])
# print(q[0])  # 队首元素
# print(q[2])  
# print(q[-1]) # 队尾元素

# q.pop()      # 弹出队尾
# print(q[-1])

# q.popleft()  # 弹出左侧（队首）
# print(q[0])  # 队首元素