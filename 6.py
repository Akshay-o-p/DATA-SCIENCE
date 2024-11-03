import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color='skyblue')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.grid(axis='y')

# Show the plot
plt.show()

# Horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(languages, popularity, color='red')
plt.title('Popularity of Programming Languages (Horizontal)')
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.grid(axis='x')

# Show the plot
plt.show()


# Different colors for each bar
colors = ['blue', 'orange', 'green', 'red', 'purple', 'cyan']

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=colors)
plt.title('Popularity of Programming Languages (Different Colors)')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.grid(axis='y')

# Show the plot
plt.show()



# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Popularity of Programming Languages (Pie Chart)')

# Show the plot
plt.show()


