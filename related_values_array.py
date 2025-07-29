
name = ["Dude", "Alice", "Luke"]
score = [42, 84, 101, 777]

min_legth = min(len(name), len(score))

for i in range(min_legth):
    names = name[i]
    scores = score[i]
    print(f"{names} got score {scores}")