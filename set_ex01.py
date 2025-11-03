from typing import List
from collections import Counter


class solv:
    def unicOccur(self, arr: List[int]):
        counter = Counter(arr)
        
        s = set()
        
        for v in counter.values():
            if v in s:
                return False
            else:
                s.add(v)
                
        return True

            

instance = solv()

result = instance.unicOccur([1, 2, 2, 1, 1, 3])

print(result)