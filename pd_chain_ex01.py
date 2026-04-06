import pandas as pd


s = pd.Series([3, 1, 4, 1, 5, 9, 2, 6])

resultado = s[s > s.mean()].sum()

print(resultado)