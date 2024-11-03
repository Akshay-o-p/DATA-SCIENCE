import pandas as pd

# Sample 2D list
data = [
    ["Alice", 24, "New York"],
    ["Bob", 27, "Los Angeles"],
    ["Charlie", 22, "Chicago"],
    ["David", 32, "Houston"]
]

# Define column names
columns = ["Name", "Age", "City"]

# Convert 2D list to DataFrame
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print("Converted DataFrame:")
print(df)
