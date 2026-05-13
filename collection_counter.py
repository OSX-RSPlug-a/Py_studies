from collections import Counter


inventory_store1 = Counter({
    "laptop": 5,
    "mouse": 8
})

inventory_store2 = Counter({
    "macbook": 3,
    "keyboard": 4
})


total_inventory = inventory_store1 + inventory_store2


print(total_inventory)