import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]  # First line data
y2 = [1, 4, 6, 8, 10]  # Second line data

# Create the plot
plt.plot(x, y1, label='Line 1', color='blue', marker='o')  # Plot line 1
plt.plot(x, y2, label='Line 2', color='red', marker='s')   # Plot line 2

# Adding titles and labels
plt.title('Multiple Lines on Same Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show legend
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()
