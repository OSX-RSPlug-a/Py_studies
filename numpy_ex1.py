import matplotlib.pyplot as plt
import numpy as np


test_array = np.array(
    [
        [3.1688358, 3.9091694, 1.66405549, -3.6188358],
        [7.1688358, -3.2588358, -9.6588358, -0.7688358],
        [2.7188358, -6.0288358, 7.4688358, 1.3088358],
    ]
)


result_array = np.where(
    test_array < 0,
    test_array * -1,
    test_array,
)


plt.figure(figsize=(8, 5))
for i, row in enumerate(result_array):
    plt.plot(row, marker="o", label=f"Row {i+1}")


plt.title("Line Graph of Array Rows")
plt.xlabel("Column Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.savefig("array_graph.png", dpi=300, bbox_inches="tight")
print("Graph saved successfully as 'array_graph.png'!")