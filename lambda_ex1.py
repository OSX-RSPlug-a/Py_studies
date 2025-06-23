def lamb():
    y = [ lambda x: x * i for i in range(4) ]
    return y

func = lamb()

result = [ funcs(2) for funcs in func ]
print(result)