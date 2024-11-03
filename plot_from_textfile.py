from locale import v

import matplotlib.pyplot as plt

# Function to read data from a text file
def read_data(filename):
    x_values = []
    y_values = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)
    return x_values, y_values

# Main function
def main():
    x, y = read_data('data.txt')  # Read data from the text file

    # Create a line plot
    plt.plot(x, y, marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel('X-axis Label')  # Change as needed
    plt.ylabel('Y-axis Label')  # Change as needed
    plt.title('Line Plot from Data')  # Change as needed

    # Show the plot
    plt.grid()
    plt.show()

if __name__ == '__main__': 
    main()
