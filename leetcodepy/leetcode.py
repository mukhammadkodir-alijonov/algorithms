from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else:
                i+=1
        return n

print(Solution().removeElement([3,2,2,3], 3)) # 2s