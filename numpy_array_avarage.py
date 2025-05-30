import numpy as np

temps = np.array([30, 32.5, 31.2, 29.9, 28.8, 35.11, 33.33, 34.4])

avg_temp = np.mean(temps)
print(f"The average temperature is: {avg_temp:.2f}°C")