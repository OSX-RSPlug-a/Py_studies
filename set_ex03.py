# union of sets
conj1 = {1, 2, 3, 4}

conj2 = {5, 6, 7, 8}

uni = conj1.union(conj2)

print(uni)


#intersection of sets
inter = conj1.intersection(conj2)

print(inter)


##intersection of sets
diff = conj1.difference(conj2)

print(diff)


#difference symetric of sets
diff_sym = conj1.symmetric_difference(conj2)

print(diff_sym)


#is subset and superset of sets
conj3 = {2, 3}

print(conj3.issubset(conj1))
print(conj3.issubset(conj2))

#is disjoint of sets
conj4 = {7, 8}

print(conj1.isdisjoint(conj4))