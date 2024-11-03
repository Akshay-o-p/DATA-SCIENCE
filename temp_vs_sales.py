import matplotlib.pyplot as plt

# Data
temperature = [12, 14, 16, 18, 20, 22, 24]
sales = [100, 200, 250, 400, 300, 450, 500]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(temperature, sales, marker='o', linestyle='-', color='b')
plt.title('Sales vs. Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales')
plt.grid()
plt.show()
