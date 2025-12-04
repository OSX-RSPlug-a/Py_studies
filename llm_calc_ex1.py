import dspy

lm = dspy.LM("ollama_chat/llama3.2:1b")
dspy.configure(lm=lm)


print("\n")

a = input("Insert the first number: ")

print("\n")

b = input("Insert the second number: ")

print("\n")

op = input("Insert type of the operation: ")


math = dspy.ChainOfThought(
    "question -> answer: float")

res = math(question=f"{a} {op} {b}")

print(res)