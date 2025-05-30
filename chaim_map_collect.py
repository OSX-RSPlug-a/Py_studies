from collections import ChainMap

toys = {'Lego': 42, 'Catasn': 24}
tech_stuff = {'keyboard-mech': 12, 'Mouse-gamer': 6}
clothes = {'Techt-shirt': 14, 'Moleton': 12}

stock = ChainMap(toys, tech_stuff, clothes)

print(stock)
print(stock['Lego'])
print(list(stock.keys()))
print(list(stock.values()))