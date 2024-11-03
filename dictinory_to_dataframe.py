import pandas as pd

# Sample dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Converted DataFrame:")
print(df)
