from typing import List

class Solv:
    
    def genParent(self, x: int) -> List[str]:
        res = []
        ans = []

        
        def bktrack(num_open, num_close):
            if num_open == num_close == x:
                ans.append(''.join(res))
                return
            
            if num_open < x:
                res.append('(')
                bktrack(num_open+1, num_close)
                res.pop()
                
            if num_close < num_open:
                res.append(')')
                bktrack(num_open, num_close+1)
                res.pop()

                
        bktrack(0, 0)
        return ans
    

print(Solv().genParent(3))