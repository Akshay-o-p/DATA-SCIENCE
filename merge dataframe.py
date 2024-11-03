import pandas as pd

df1 = pd.DataFrame({
    "eid": [1, 2, 3, 4],
    "ename": ["Alice", "Bob", "Charlie", "David"],
    "stipend": [3000, 4000, 2500, 3500]
})

df2 = pd.DataFrame({
    "eid": [1, 2, 3, 5],
    "designation": ["Manager", "Developer", "Designer", "Intern"]
})

merged_df = pd.merge(df1, df2, on="eid", how="left")

merged_df.rename(columns={"designation": "position"}, inplace=True)

print("Merged DataFrame:")
print(merged_df)
