import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 27, 22, 32, 27],
    "Score": [88, 92, 85, 91, 87]
}

df = pd.DataFrame(data)


sorted_df = df.sort_values(by=["Age", "Score"], ascending=[True, False])


print("Sorted DataFrame:")
print(sorted_df)
