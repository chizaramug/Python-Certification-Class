import numpy as np 
import matplotlib.pyplot as plt

# Generate values for t within the interval 2 < t < 4
t = np.linspace(2, 4, 1000)  # Create 1000 evenly spaced values between 2 and 4

# Calculate the corresponding values of y
y = np.sin(np.pi * t)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='y = sin(πt)', color='blue')
plt.title('Graph of y = sin(πt) for 2 < t < 4')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
