import matplotlib.pyplot as plt

# Sample data points
x_sin = [0, 1, 2, 3, 4, 5]
y_sin = [0, 0.84, 0.91, 0.14, -0.76, -0.99]  # Sine function data points

x_cos = [0, 1, 2, 3, 4, 5]
y_cos = [1, 0.54, -0.42, -0.99, -0.76, 0.28]  # Cosine function data points

x_tan = [0, 1, 2, 3, 4, 5]
y_tan = [0, 1.56, -2.44, -0.14, 1.57, 3.38]  # Tangent function data points

x_linear = [0, 1, 2, 3, 4, 5]
y_linear = [0, 1, 2, 3, 4, 5]  # Linear function data points

# Create multiple plots
plt.figure(figsize=(10, 8))

# First plot (Sine)
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.plot(x_sin, y_sin, color='blue', marker='o')
plt.title('Sine Function')
plt.xlabel('X-axis')
plt.ylabel('sin(x)')
plt.grid(True)

# Second plot (Cosine)
plt.subplot(2, 2, 2)  # 2nd subplot
plt.plot(x_cos, y_cos, color='red', marker='s')
plt.title('Cosine Function')
plt.xlabel('X-axis')
plt.ylabel('cos(x)')
plt.grid(True)

# Third plot (Tangent)
plt.subplot(2, 2, 3)  # 3rd subplot
plt.plot(x_tan, y_tan, color='green', marker='^')
plt.title('Tangent Function')
plt.xlabel('X-axis')
plt.ylabel('tan(x)')
plt.ylim(-5, 5)  # Limit y-axis for better visualization
plt.grid(True)

# Fourth plot (Linear)
plt.subplot(2, 2, 4)  # 4th subplot
plt.plot(x_linear, y_linear, color='purple', marker='x')
plt.title('Linear Function')
plt.xlabel('X-axis')
plt.ylabel('x')
plt.grid(True)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
