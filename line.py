import matplotlib.pyplot as plt

# Define the points0
x = [1, 2, 6, 18]
y = [3, 10, 12, 20]

# Create a new figure
plt.figure()

# Plot the line with dotted style
plt.plot(x, y, color='red', linestyle=':', marker='o', markerfacecolor='green')

# Mark each point
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.text(xi, yi, f"({xi}, {yi})", fontsize=9, ha='right')

# Set the title and labels
plt.title("Line Diagram with Specified Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the grid
plt.grid()

# Show the plot
plt.show()
