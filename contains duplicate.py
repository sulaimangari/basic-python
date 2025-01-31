from typing import List

nums = [1,2,3,4,5,1] 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

solution = Solution()
print(nums,'>>',solution.hasDuplicate(nums))

