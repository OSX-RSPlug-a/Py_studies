from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            
            if comp in val:
                return [val[comp], i]
            
            val[num] = i
        
        raise ValueError("No two sum solution")

    
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))