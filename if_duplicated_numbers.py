from typing import List

nums = [1, 2, 3, 1, 2, 3]

k = 2

class solv:
    def containsNearDupl(self, nums: List[int], k : int):
        num_to_i = {}
        n = len(nums)
        
        for i in range(n):
            if nums[i] in num_to_i:
                if abs(num_to_i[nums[i]] - i) <= k:
                    return True
            
            num_to_i[nums[i]] = i
        
        return False
        
        
solver = solv()
result = solver.containsNearDupl(nums, k)
print(result)