import pytest

class Solution:
    def numJewelsStones(self, jewels, stones):
        jewels = set(jewels)
        
        num_jewels = 0
        
        for s in stones:
            if s in jewels:
                num_jewels += 1
        return num_jewels
        

##################### test ####################
sol = Solution()

test_cases = [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZZ", 0),
    ("abc", "aabbcc", 6),
    ("", "abc", 0),
    ("a", "", 0)
]

print("################### Running Tests ###################")

for i, (j, s, expected) in enumerate(test_cases):
    result = sol.numJewelsStones(j, s)
    
    if result == expected:
        print(f"Test {i+1}: PASSED (Expected {expected}, got {result})")
    else:
        print(f"Test {i+1}: FAILED (Expected {expected}, got {result})")
        

##################### test ####################    
def test_jewels():
    sol = Solution()
    
    assert sol.numJewelsStones("aA", "aAAbbbb") == 3
    
    assert sol.numJewelsStones("z", "ZZZ") == 0
    
    assert sol.numJewelsStones("abc", "aabbcc") == 6
    
    assert sol.numJewelsStones("", "") == 0
    