
name = ["Dude", "Alice", "Luke"]
score = [42, 84, 777, 102]

for names, scores in zip(name, score):
    print(f"{names} got score {scores}")