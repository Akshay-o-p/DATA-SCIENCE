import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

print("Original DataFrame with Custom Indexing:")
print(df)


df_reset = df.reset_index(drop=True)

print("\nDataFrame with Default Indexing:")
print(df_reset)
