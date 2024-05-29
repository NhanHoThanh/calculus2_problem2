


def r1(z):
    return np.cos(-z - 1)**-1


def r2(z):
    return np.cos(-2*z - 1)**-1


firstR = r1(-2)
secondR = r2(-2)
print(firstR)
print(secondR)
print(np.pi*(firstR**2 - secondR**2))

# Define the parameter ranges
r = np.linspace(0, np.pi, 100)