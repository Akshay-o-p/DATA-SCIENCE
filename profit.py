import pandas as pd


data = {
    "cname": ["Company A", "Company B", "Company C", "Company D"],
    "profit": [10000, -5000, 25000, 0]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


df["profit"] = df["profit"] > 0

print("\nDataFrame after converting profit values to boolean:")
print(df)
