import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a + 5)
print("\n")
print("\n")

# another tests
b = np.array([1, 2, 3, 4, 5])
c = np.array([6, 7, 8, 9, 10])

print(b + c)
print(b * c)
print(b - c)
print(b / c)
print(b ** 2)
print(f"Dot product of b and c: {np.dot(b, c)}")
print("\n")
print("\n")

# more tests
d = np.array([5, 10, 15, 20, 25])

print(f"Sum of d: {np.sum(d)}")
print(f"Mean of d: {np.mean(d)}")
print(f"Max of d: {np.max(d)}")
print(f"Min of d: {np.min(d)}")
print(f"Standard deviation of d: {np.std(d)}")
print(f"Variance of d: {np.var(d)}")
print(f"Median of d: {np.median(d)}")