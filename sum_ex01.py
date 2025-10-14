from typing import List

class Solv:
    def two_Sum(self, numbers: List[int], target: int):
        n = len(numbers)
        l = 0
        r = n-1
        
        
        while  l < r:
            summ = numbers[l] + numbers[r]
            
            if summ == target:
                return [l + 1, r +1]
            elif summ < target:
                l += 1
            else:
                r -= 1
        return []



solver = Solv()


test_cases = [
    ([2, 7, 11, 15], 9, [1, 2]),          
    ([1, 2, 3, 4, 4], 8, [4, 5]),        
    ([-1, 0, 5, 10], 9, [3, 4]),          
    ([10, 20, 30, 40], 70, [3, 4]),       
    ([5, 10, 15, 20], 100, []),           
]


print("##### Two Sum (Sorted Array) Tests #####")


for numbers, target, expected in test_cases:
 
    result = solver.two_Sum(numbers, target)
    

    is_correct = result == expected
    
    print(f"\nInput Numbers: {numbers}")
    print(f"Target:        {target}")
    print(f"Result:        {result}")
    print(f"Expected:      {expected}")
    print(f"PASS/FAIL:     {'PASS' if is_correct else 'FAIL'} (Indices are 1-based)")