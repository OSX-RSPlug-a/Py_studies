from typing import List
import math


class Solv:
    def minSpeed(self, piles: List[int], h: int):
        left = 1
        right = max(piles)
        
        while left < right:
            middle = (left + right) // 2
            hour_spent = 0
            
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
                
            
            if hour_spent <= h:
                right = middle
            else: 
                left = middle + 1
            
        return right 
    

#--- testing ---
def run_tests():
    
    s = Solv()
    
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1, 1, 1, 999999999], 10, 100000000)
    ]
    
    print("Running Tests for minSpeed function")
    
    all_passed = True
    
    for piles, h, expected in test_cases:
        actual = s.minSpeed(piles, h)
        
        test_status = "PASS" if actual == expected else "FAIL"
        
        if actual != expected:
            all_passed = False
            
        print(f" Piles: {piles}, H: {h}")
        print(f"  Expected Speed: {expected}, Actual Speed: {actual} -> **{test_status}**")
        print("-" * 20)

    if all_passed:
        print("\n All test cases passed successfully! ")
    else:
        print("\n Some test cases failed. Review it.")


if __name__ == "__main__":
    run_tests()