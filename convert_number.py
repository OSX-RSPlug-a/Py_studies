class solv:
    def titleNumber(self, columnTitle: str) -> int:

        h = {chr(i): i - 64 for i in range(65, 91)}
        s = columnTitle
        n = len(s)
        
        ret = 0
        mult = 1
        
        for i in range(n - 1, -1, -1):
            ret += h[s[i]] * mult
            mult *= 26
        
        return ret


solver = solv()
    

solver = solv
print(solver.titleNumber("A","AA"))
print(solver.titleNumber("Z","AA"))
