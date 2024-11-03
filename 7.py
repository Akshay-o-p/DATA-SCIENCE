import numpy as np
import matplotlib.pyplot as plt

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Set up the bar width and positions
bar_width = 0.35
x = np.arange(len(groups))  # the label locations

# Create the bar plot
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - bar_width/2, means_men, width=bar_width, label='Men', color='blue')
bars2 = plt.bar(x + bar_width/2, means_women, width=bar_width, label='Women', color='pink')

# Adding labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)  # Set the x ticks to the group names
plt.legend()

# Show grid
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()
