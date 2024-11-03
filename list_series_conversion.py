import pandas as pd

# Sample list
my_list = [10, 20, 30, 40, 50]

# Convert list to Series
my_series = pd.Series(my_list)

print("Original List:", my_list)
print("Converted Series:")
print(my_series)
