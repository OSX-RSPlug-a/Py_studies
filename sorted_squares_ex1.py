from typing import List

class solv:
    def sortedSquare(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [0] * n
        
        L, R = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                val = nums[L]
                
                L += 1
            else:
                val = nums[R]
                
                R -= 1

            
            res[i] = val ** 2
            
        return res



s = solv()

result = s.sortedSquare([-4, -1, 0, 3, 10])

print(result)