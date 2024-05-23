import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 10

# Define the parameter ranges
r = np.linspace(0, np.pi, 100)
p = np.linspace(0, 2 * np.pi, 100)

r, p = np.meshgrid(r, p)

# Surface b
x_b = r * np.cos(p)
y_b = r * np.sin(p)
z_b = -1 - np.cos(r)

# Surface c
x_c = r * np.cos(p)
y_c = r * np.sin(p)
z_c = -0.5 - 0.5 * np.cos(r)

# Plotting
fig = plt.figure(figsize=(12, 6))

# Create a single 3D plot
ax = fig.add_subplot(111, projection='3d')

# Plot surface b
ax.plot_surface(x_b, y_b, z_b, cmap='viridis', alpha=0.5)

# Plot surface c
ax.plot_surface(x_c, y_c, z_c, cmap='plasma', alpha=0.5)


ax.set_title('Surfaces b and c')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


plt.show()
