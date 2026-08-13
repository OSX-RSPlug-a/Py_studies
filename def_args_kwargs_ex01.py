#simple function
def show_datas(name, age):
    print(f"Full_Name: {name}, Full_Age: {age}")



show_datas("Dude42", 42)


# args
def soms(*numbers):
    som1 = sum(numbers)

    print(f"Soma: {soms}")


soms(2, 4, 6)


#kwargs
def show_info(**datas):
    for chave, valor in datas.items():
        print(f"{chave}: {valor}")


show_info(name="Katia", age=22, city="Sao Paulo")