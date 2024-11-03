import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Occupation": ["Engineer", "Doctor", "Engineer", "Artist", "Doctor", "Artist"],
    "Salary": [70000, 120000, 80000, 50000, 110000, 60000]
}

df = pd.DataFrame(data)

avg_salary_per_occupation = df.groupby("Occupation")["Salary"].mean()

print("Average Salary per Occupation:")
print(avg_salary_per_occupation)
