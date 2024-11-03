import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)


first_two_rows = df.head(2)

print("First 2 rows of the DataFrame:")
print(first_two_rows)