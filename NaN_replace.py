import pandas as pd
import numpy as np


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, np.nan, 22, 32],
    "Salary": [70000, 120000, np.nan, 50000]
}

df = pd.DataFrame(data)

print("Original DataFrame with NaN values:")
print(df)


df_filled = df.fillna(0)

print("\nDataFrame after filling NaN values with 0:")
print(df_filled)
