import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 10


def r1(z):
    if not (-2 <= z <= 0):
        raise ValueError("z must be in the range -2 <= z <= 0")
    return np.arccos(-z - 1)


def r2(z):
    if not (-1 <= z <= 0):
        raise ValueError("z must in range -1 0")
    return np.arccos(-2*z - 1)


firstR = r1(-2)
secondR = r2(0)
print(firstR)
print(secondR)
print(firstR**2)
print(secondR**2)
print(np.pi*(firstR**2 - secondR**2))

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

# for z in np.linspace(0, -1, 5):
#     x = r1(z)
#     y = r2(z)
#     z = np.full_like(x, z)  # Create a 2D array for z
#     ax.plot_surface(x, y, z, color='b', alpha=0.5)


ax.set_title('Surfaces b and c')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

z_values = np.linspace(0, -2, n+1)

# Calculate r1 and r2 for each z value
# r1_values = r1(z_values)
# r2_values = r2(z_values)

# Print the results
P1 = 0
P2 = 0
for z in z_values:
    print("z value: {}".format(z))
    if (0 >= z > -1):
        print("r1: {} r1^2: {}".format(r1(z), r1(z)**2))
        print("r2: {} r2^2: {}".format(r2(z), r2(z)**2))
        print("Area: pi*(r1^2 - r2^2) = {}".format(np.pi*(r1(z)**2 - r2(z)**2)))
        P1 += np.pi*(r1(z)**2 - r2(z)**2)
    if (-1 >= z >= -2):
        print("r1: {} r1^2: {}".format(r1(z), r1(z)**2))
        print("Area: pi*r1^2 =  {}".format(np.pi*r1(z)**2))
        P2 += np.pi*r1(z)**2

print(P1)
print(P2)
print("Total Area: {}".format(P1 + P2))


# plt.show()

###############################################################################################################
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# n = 10


# def r1(z):
#     return np.cos(-z - 1)**-1


# def r2(z):
#     return np.cos(-2*z - 1)**-1


# # Define the parameter ranges
# r = np.linspace(0, np.pi, 100)
# p = np.linspace(0, 2 * np.pi, 100)

# r, p = np.meshgrid(r, p)

# # Surface b
# x_b = r * np.cos(p)

# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Draw annuli from z = 0 to z = -1
# for z in np.linspace(0, -1, 5):
#     x = r1(z) * np.cos(p)
#     y = r1(z) * np.sin(p)
#     z = np.full_like(x, z)  # Create a 2D array for z
#     ax.plot_surface(x, y, z, color='b', alpha=0.5)

# # Draw circles from z = -1 to z = -2
# for z in np.linspace(-1, -2, 5):
#     x = r2(z) * np.cos(p)
#     y = r2(z) * np.sin(p)
#     z = np.full_like(x, z)  # Create a 2D array for z
#     ax.plot_surface(x, y, z, color='r', alpha=0.5)
# plt.show()
