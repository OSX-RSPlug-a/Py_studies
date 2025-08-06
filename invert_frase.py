class invert_frase:
    def reverseWords(self, s: str) -> str:
        new_s = ' '.join(s.split(' ')[::-1]).strip(' ')
        
        ret = []
        i = 0
        while i < len(new_s):
            if i < len(new_s) - 1 and new_s[i] == new_s[i+1] == ' ':
                i += 1
            else:
                ret.append(new_s[i])
                i += 1
                
        return ''.join(ret)


inverter = invert_frase()


frase_1 = "Hello there. It's a trap"
print(inverter.reverseWords(frase_1))
