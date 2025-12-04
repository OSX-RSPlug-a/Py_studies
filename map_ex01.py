from typing import List

prices = [11.20, 25.99, 51.00, 100.10]


def tax_apply(price: float) -> float:
     return round(price * 1.5, 2)

    

taxed_price = []
for price in prices:
    new_price = tax_apply(price)
    taxed_price.append(new_price)

print("############################# Ex without map ##################################")
print(taxed_price)
print("############################# !!!!!!!!!!!!!! ##################################")


print("############################# Ex using map ##################################")
taxed_price_mapped = list(map(tax_apply, prices))
print(taxed_price_mapped)