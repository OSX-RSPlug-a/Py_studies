import random

tuple_frutas = ("apple", "banana", "cherry")
print(tuple_frutas[2])
print(len(tuple_frutas))
print(tuple_frutas)

item_randomico = random.choice(tuple_frutas)
print(f"A palavra randomica: {item_randomico}")