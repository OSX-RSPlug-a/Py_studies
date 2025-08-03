

class Column:
    def rows(self, columnTitle: str) -> int:
        h = {
            chr(i) : i-64 for i in range(65, 65+26)
            }
        s =  columnTitle
        n = len(s)
        
        ret = 0
        mult = 1
        
        for i in range(n-1, -1, -1):
            ret += h[s[i]] * mult
            mult *= 26
            
        return ret


sheet = Column()
sheet.rows("AB")