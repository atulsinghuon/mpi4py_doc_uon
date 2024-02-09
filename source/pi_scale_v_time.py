# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:33:55 2024

@author: uizas3
"""
import matplotlib.pyplot as plt
procs = [4, 8, 16, 32]
time = [0.588, 0.301, 0.254, 0.261]

# Plotting the bar chart
plt.bar(procs, time, color='skyblue')

# Adding labels and title
plt.xlabel('Number of Processors')
plt.ylabel('Time (s)')
plt.title('Time vs Number of Processors')

# Set the y-axis limits to [0, 1]
plt.ylim(0, 1)
plt.xticks(procs)

# Show the plot
plt.show()
