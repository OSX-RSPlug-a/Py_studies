
lettters = ["a", "b", "c", "d"]

out = []

for ch in lettters:
    if ch < "c":
        out.append(ch)
    
    lettters.remove(ch)
    

size = len(lettters) + len(out)

print(size)